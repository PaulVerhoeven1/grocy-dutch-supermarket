# Grocy dutch supermarkets product scraper
These are two Python script that connect with the dutch supermarket [Jumbo.com](https://jumbo.com) or [ah.nl](https://ah.nl).
It uses the python package [SupermarktConnector](https://github.com/bartmachielsen/SupermarktConnector) from [Bart Machielsen](https://github.com/bartmachielsen/) for this.
The scripts download the product information from the API's.
It then post this information to [Grocy](https://github.com/grocy/grocy) .

## Getting started

1. `git clone git@github.com:baskraai/grocy-dutch-supermarket.git; cd grocy-dutch-supermarket`
2. `pip3 install -r requirements.txt`
3. `chmod +x *.py`
4. `cp .env_example .env`
5. Edit the configration in the .env file.

## How to use this script

Run the script with as argument the EAN / Barcode, example:
```
./jumbo-grocy.py 8710391936834
./ah-grocy.py 8710391936834
```

## Todo
- [x] Add the possiblity to use arguments with the script.
- [ ] Merging AH and Jumbo scripts into one file.
- [ ] Creating a script to scrape more information from the Jumbo.com website.
- [ ] Add logging.
- [ ] Add `try` and `except` blocks.
- [ ] Creating a Dockerfile to run the script within a container.

