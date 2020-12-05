# Grocy jumbo.com connector
This is a Python script that connects with the dutch supermarket [Jumbo.com](jumbo.com)throught the python package [SupermarktConnector](https://github.com/bartmachielsen/SupermarktConnector). The script downloads product information and posting those information (title and image) to the self-hosted grocery management solution [Grocy](https://github.com/grocy/grocy).

**Getting started:**
* install the required packages with pip (pip install -r requirements.txt)
* Create .env file in the same directory where where you run this code. There is an .env_example file that you can use ase baseline

**Planned refinements:**
- [ ] Adding the possiblity to use arguments with the script
- [ ] Creating a script to scrape more information from the Jumbo.com website
- [ ] Creating a Dockerfile to run the script within a container