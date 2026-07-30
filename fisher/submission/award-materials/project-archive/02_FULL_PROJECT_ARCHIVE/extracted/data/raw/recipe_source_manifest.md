# Recipe Source Manifest

Created/verified: 2026-04-28

## Staged source files

| Local path | Size bytes | Source URL |
|---|---:|---|
| `data/raw/recipes_long.txt` | 11524282 | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_long.txt |
| `data/raw/recipes_cuisines.txt` | 385047 | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines.txt |
| `data/raw/recipes_cuisines_count.txt` | 277 | https://raw.githubusercontent.com/zdealveindy/anadat-r/master/data/recipes_cuisines_count.txt |

## Schema notes

`recipes_long.txt` is tab-delimited with columns `id`, `cuisine`, and `ingredients`.
`recipes_cuisines.txt` is a wide cuisine × ingredient count table.
`recipes_cuisines_count.txt` is a cuisine-level recipe count table.

## Usage note

The prepared files are public on GitHub, but the underlying dataset is described as Kaggle/Yummly-derived. Treat as prototype input unless Run 3 confirms final-use permissions.
