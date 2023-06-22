# Oklahoma Cooling Centers Python

[Oklahoma Cooling Centers](https://alex-code4okc.github.io/oklahoma_cooling_centers_python/)

Python project to generate webpage map of Oklahoma Cooling centers.

## Dependencies
* [Folium](https://github.com/python-visualization/folium)
* [Pandas](https://github.com/pandas-dev/pandas)

## Quickstart
```bash
# create virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install dependencies
python3 -m pip install -r requirements.txt

# run script
python3 makeMap.py

# open map in browser
open ./docs/index.html

# deactivate virtual environment
deactivate
```

## TODO
* [Issues](https://github.com/alex-code4okc/oklahoma_cooling_centers_python/issues)
* [asdf](https://asdf-vm.com/) + [poetry](https://python-poetry.org/)
* Open locations on map in [new tab](https://www.freecodecamp.org/news/how-to-open-a-link-in-a-new-tab/)
* CI (GitHub Actions)
  * e.g., [renovate](https://github.com/marketplace/renovate) or [dependabot](https://github.com/dependabot)
* Rename `makeMap.py` to `main.py` or `make_map.py`
  * Not a [class](https://peps.python.org/pep-0008/#package-and-module-names), sir
