# Contributing & moderation policy

Suggest a project by opening an issue ("Suggest a project") or a pull request that adds
an entry to `projects.yml`. Don't edit the tables in `README.md` directly. Regenerate them with:

```sh
pip install pyyaml
python scripts/curate.py render
```

## Inclusion criteria

A project is accepted only if **all** of these hold:

1. **Open source.** It has an open-source license (preferably OSI-approved). If GitHub can't detect it
   (dual licenses, unusual file names), a moderator reads the license file and records it in `license:`.
   "Source available" or no license at the repository root is rejected.
2. **ESP32 is a primary target.** The project is built for ESP32 / S2 / S3 / C3 / C6 / H2 / P4 modules, not just "might compile on it".
3. **Acclaimed.** It has **500+ GitHub stars**, *or* an `acclaim:` link to notable independent coverage (e.g. a Hackaday feature, a conference talk, a major maker publication).
4. **Alive.** It isn't archived and has had a push within the last **24 months**.
5. **Buildable.** The README documents the hardware needed and how to flash or build.
6. **Not a duplicate.** Forks are only listed if they have clearly overtaken the original.

The following are also rejected: closed firmware blobs sold as "open", projects whose main purpose is harming others,
and self-promotion that doesn't meet the bar above. Security research tools are allowed when they are established,
widely used, and carry a `note:` reminding users to test only on equipment they're authorized to test.

## Removal

The weekly **audit** workflow checks every entry against criteria 1, 3 and 4 and fails if something breaks them
(archived, moved, no longer licensed, inactive). A moderator then either fixes the entry (e.g. updates a
moved repo), or removes it in a PR that explains why.

## Entry format

```yaml
- name: WLED
  repo: wled/WLED
  category: lighting            # a key from `categories:`
  description: Addressable LED strip controller with 100+ effects   # <= 120 chars, no trailing period
  hardware: true                # optional: schematics/PCB are published
  license: MIT AND GPL-3.0-only # optional: verified SPDX, only if GitHub can't detect it
  acclaim: https://hackaday.com/...   # optional: needed if under 500 stars
  note: Moderator note          # optional: shown in the README
```
