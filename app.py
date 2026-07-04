from flask import Flask, render_template

from scrapers.amazon import scrap_amazon_data

from scrapers.mutualfunds import scrap_mutualfund_data

from scrapers.yahoofinance import scrap_finance_data

from scrapers.collegedunia import scrap_college_data

from scrapers.goodreads import scrap_quotes_data

from scrapers.imdb import scrap_imdb_data

from scrapers.bbc import scrap_bbc_data

from scrapers.automationexercise import scrap_automationexercise_data

from scrapers.booking import scrap_booking_data

from scrapers.spotify import scrap_spotify_data

from scrapers.concurrency import scrape_concurrency_data

from scrapers.products import scrape_products_data

from scrapers.jikan import scrape_jikan_data

from scrapers.recipefinder import scrape_recipe_data

from scrapers.pokemon import scrape_pokemon_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

@app.route('/learnmore')
def learnmore():
    return render_template("learnMore.html")

@app.route('/scraping')
def scraping():
    return render_template("scraping.html")

@app.route('/staticscraping')
def staticscraping():
    return render_template("static.html")

@app.route('/amazon')
def amazon():
    products=scrap_amazon_data()
    return render_template("amazon.html",products=products)

@app.route('/mutualfunds')
def mutualfunds():
    funds=scrap_mutualfund_data() 
    return render_template("mutualfunds.html",funds= funds)

@app.route("/yahoofinance")
def yahoofinance():
    currencies = scrap_finance_data()
    return render_template("yahoofinance.html",currencies=currencies)


@app.route("/collegedunia")
def collegedunia():
    colleges = scrap_college_data()
    return render_template("collegedunia.html",colleges=colleges)


@app.route("/goodreads")
def goodreads():
    quotes = scrap_quotes_data()
    return render_template("goodreads.html",quotes=quotes)

@app.route("/dynamicscraping")
def dynamic_scraping():
    return render_template("dynamicscraping.html")

@app.route("/imdb")
def imdb():
    products = scrap_imdb_data()
    return render_template("imdb.html", products=products)

@app.route("/bbc")
def bbc():
    products = scrap_bbc_data()
    return render_template("bbc.html", products=products)

@app.route("/automationexercise")
def automationexercise():
    products = scrap_automationexercise_data()
    return render_template("automationexercise.html",products=products)

@app.route("/booking")
def booking():
    hotels = scrap_booking_data()
    return render_template("booking.html",hotels=hotels)

@app.route("/spotify")
def spotify():
    songs = scrap_spotify_data()
    return render_template("spotify.html",songs=songs)

@app.route("/api")
def api():
    return render_template("APIscraping.html")

@app.route("/concurrency")
def concurrency():
    products = scrape_concurrency_data()
    return render_template("concurrency.html", products=products)

@app.route("/products")
def products():
    products = scrape_products_data()
    return render_template("products.html",products=products)

@app.route("/jikan")
def jikan():
    anime = scrape_jikan_data()
    return render_template("jikan.html",anime=anime)

@app.route("/recipefinder")
def recipefinder():
    recipes = scrape_recipe_data()
    return render_template("recipefinder.html",recipes=recipes)

@app.route("/pokemon")
def pokemon():
    pokemon = scrape_pokemon_data()
    return render_template("pokemon.html",pokemon=pokemon)

if __name__ == "__main__":
    app.run(debug=True)