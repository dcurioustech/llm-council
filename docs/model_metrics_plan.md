# Per-model latency & token badges

## Goal

Show how long each council model took and how many tokens it used, directly on
its tab in the UI, so users can compare speed and cost across the council.

## Approach

### Backend (phase0)

- `backend/openrouter.py` `query_model()` times the request with
  `time.perf_counter()` and adds two keys to its returned dict:
  - `latency_ms` (int, wall-clock milliseconds for the HTTP call)
  - `usage` (the `usage` object from the OpenRouter response, or `None` if absent)
- `backend/council.py` copies `latency_ms` and `usage` into every Stage 1 result,
  every Stage 2 result, and the Stage 3 result, alongside the existing keys.
- Failure behavior is unchanged: a failed model still returns `None` and is skipped.
- No new endpoints. Both `/message` and `/message/stream` carry the new fields
  automatically because they are part of the stage payloads.

### Frontend (phase1)

- New `frontend/src/components/ModelMetrics.jsx` renders a compact badge, e.g.
  `⏱ 3.2s · 1,240 tok`. It renders nothing when both values are missing (old
  stored conversations have neither).
- `Stage1.jsx` and `Stage2.jsx` show the badge next to the model name in the
  active tab's content. `Stage3.jsx` shows it for the chairman.
- Styling lives in a small `ModelMetrics.css`, consistent with the existing
  light theme (primary `#4a90e2`).

## Out of scope

Cost in dollars, persistence of historical analytics, charts.
