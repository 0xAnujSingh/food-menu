from flask import Flask, request
from app import MenuItem, Menu

app = Flask(__name__)

@app.route('/lists', methods = ['POST'])
def createList():
    data = request.json

    title = data['title']

    newList = Menu.new(title)

    return newList.toJSON()

@app.route('/lists')
def getAllMenuLists():
    lists = Menu.listAllMenu()
    result = []

    for li in lists:
        result.append(li.toJSON())

    return {
        "lists": result
        }

@app.route('/lists/<menuId>')
def getListById(menuId):
    lists = Menu.menuById(menuId)
    result = []

    for li in lists:
        result.append(li.toJSON())

    return {
        "menuId" : result
    }

@app.route('/lists/<menuId>/item', methods = ['POST'])
def createItem(menuId):
    item = MenuItem.new(menuId)
    return item.toJSON()

@app.route('/lists/<menuId>/item')
def getAllItems(menuId):
    item = MenuItem.findByMenu(menuId)
    result = []
    for i in item:
        result.append(i.toJSON())

    return {
        "menuId" : result
        }

@app.route('/lists/<menuId>/item/<id>')
def getItemById(menuId,id):
    item = MenuItem.findById(menuId, id)
    result = []

    for i in item:
        result.append(i.toJSON())

    return {
        "menuId" : menuId,
        "id" : id
    }



