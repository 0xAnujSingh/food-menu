from logging import exception
from flask import Flask, request
from app import MenuItem, Menu, Restaurant

app = Flask(__name__)

@app.route('/restaurant', methods = ['POST'])
def createRestaurant():
    try:
        data = request.json
        title = data['title']
        newRestaurant = Restaurant.new(title)

        return newRestaurant.toJSON()
    except Exception as e:
        return {
            "error" : str(e)
        }

@app.route('/restaurant')
def listAllRestaurant():
    Restaurants = Restaurant.listAllRestaurant()
    result = []
    for li in Restaurants:
        result.append(li.toJSON())
    return {
        "Restaurants" : result
    }

@app.route('/restaurant/<rId>')
def getRestaurantById(rId):
    try:
        restaurant = Restaurant.listById(rId)

        return {
            "restaurant" : restaurant.toJSON()
        }
    except Exception as e:
        return {
            "e" : str(e)
        }

@app.route('/restaurant/<rId>/menu')
def fromRestaurantGetMenu(rId):
    menus = Menu.getByResaurantId(rId)
    result = []
    for i in menus:
        result.append(i.toJSON())

    return {
        "menus" : result
    }

@app.route('/menu', methods = ['POST'])
def createMenu():
    try:
        data = request.json

        title = data['title']
        rId = data['rId']

        newMenu = Menu.new(title, rId)

        return newMenu.toJSON()
    except Exception as err:
        return {
            "error" : str(err)
            }
         

@app.route('/menu')
def getAllMenu():
    menus = Menu.listAllMenu()
    result = []

    for li in menus:
        result.append(li.toJSON())

    return {
        "menus": result
        }

@app.route('/menu/<menuId>')
def getMenuById(menuId):
    try:
        menu = Menu.menuById(menuId)

        return {
            "menu" : menu.toJSON()
        }
    except Exception as err: 
        return {
            "err" : str(err)
            }

@app.route('/menu/<menuId>/item', methods = ['POST'])
def createItem(menuId):
    try:
        data = request.json
        title = data['title']
        price = data['price']
        item = MenuItem.new(menuId, title, price)

        return item.toJSON()
    except Exception as err:
        return {
            "err" : str(err)
        }

@app.route('/menu/<menuId>/item')
def getAllItems(menuId):
    item = MenuItem.findByMenu(menuId)
    result = []
    for i in item:
        result.append(i.toJSON())

    return {
        "menuId" : result
        }

@app.route('/menu/<menuId>/item/<id>')
def getItemById(menuId, id):
    try:
        item = MenuItem.findById(id)

        return {
            "item" : item.toJSON()
        }
    except Exception as err:
        return {
            "err" : str(err)
        }

if __name__ == "__main__":
    app.run()



