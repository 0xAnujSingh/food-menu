from logging import error, exception
from sqlite3.dbapi2 import Error
from flask import Flask, request
from app import MenuItem, Menu

app = Flask(__name__)


@app.route('/menu', methods = ['POST'])
def createMenu():
    try:
        data = request.json

        title = data['title']

        newMenu = Menu.new(title)

        return newMenu.toJSON()
    except Exception as err:
        return {
            "error" : str(err)
            }
         

@app.route('/menu')
def getAllMenu():
    lists = Menu.listAllMenu()
    result = []

    for li in lists:
        result.append(li.toJSON())

    return {
        "lists": result
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



