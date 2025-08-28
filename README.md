# CCTV Smart Guard — Ethical MVPs

**Purpose:** Add an AI layer on top of existing CCTV feeds to provide **workplace safety**, **crowd-density monitoring**, and **queue-management** without identifying people. All processing is local/edge-first, faces are blurred by default, and face-matching is optional and limited to a small consented whitelist (OFF by default).

**MVPs included:**
1. Workplace Safety Compliance (PPE detection)
2. Crowd Density & Evacuation Support (people counting + heatmaps)
3. Queue Management (queue length detection + alerts)

## How to upload to Blackbox.ai (short)
1. Create a new repository on your local machine with the file list above.
2. `git init` and commit files.
3. Push to a remote (GitHub/GitLab).
4. In Blackbox.ai, choose "Import from Git" or upload the repository ZIP. Add the run command `python app.py --config config.json` or a Dockerfile if you create one.

## Ethical checklist
* [ ] `face_matching_enabled` = false by default.
* [ ] Blurring enabled.
* [ ] Local-only processing instructions included.
* [ ] Privacy policy file present.
* [ ] Demo script requires operator confirm before escalation.