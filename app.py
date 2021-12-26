import sqlite3
from db import conn

class MenuItem:
  def __init__(self, itemId, itemName, price, menuId):
    self.id = itemId
    self.name = itemName
    self.price = price
    self.menuId = menuId

  def toJSON(self):
    return {
      "itemId" : self.id,
      "itemName" : self.name,
      "price" : self.price,
      "menuId" : self.menuId
    }

  ## store a new item
  @classmethod
  def new(cls, menuId, name, price):
    cursor = conn.cursor()
    data = None

    try:
      cursor.execute("INSERT INTO item(`menuId`, `name`,`price`) VALUES (?, ?, ?);", (menuId, name, price, ))
      cursor.execute("SELECT `id`, `name`, `price`, `menuId` FROM `item` WHERE `id` = ?", (cursor.lastrowid, ))
      data = cursor.fetchone()

      conn.commit()
    except Exception as err:
      raise err
    finally:
      cursor.close()

    return cls(data[0], data[1], data[2], data[3])

  @classmethod
  def findByMenu(cls, menuId):

    cursor = conn.cursor()
    result = []
    data = None

    try:
      cursor.execute("SELECT `id`, `name`, `price`, `menuId` FROM `item` WHERE `menuId` = ?;",(menuId, ))
      data = cursor.fetchall()
    except:
      raise Exception("Error : unable to fetch data")
    finally:
      cursor.close()

    for item in data:
      result.append(cls(item[0], item[1], item[2], item[3]))

    return result

  @classmethod
  def findById(cls, id):
    cursor = conn.cursor()
    data = None

    try:
      cursor.execute("SELECT `id`, `name`, `price`, `menuId` FROM `item` WHERE `id` = ?;", (id, ))
      data = cursor.fetchone()

    except Exception as err:
      return err
    finally:
      cursor.close()

    if data is None:
      return None

    return cls(data[0], data[1], data[2], data[3])




class Menu:
  def __init__(self, menuId, title):
    self.name =[]
    self.menuId = menuId
    self.title = title

  @classmethod
  def new(cls, title):
    cursor = conn.cursor()
    data = None

    try:
      cursor.execute("INSERT INTO menu(`title`) VALUES (?);", (title, ))
      cursor.execute("SELECT `menuId`, `title` FROM `menu` WHERE `menuid` = ?", (cursor.lastrowid, ))
      data = cursor.fetchone()

      conn.commit()
    except Exception as e:
      raise e
    finally:
      cursor.close()

    return cls(data[0], data[1])


  @classmethod
  def listAllMenu(cls):
    cursor = conn.cursor()
    data = None
    result = []

    try:
      cursor.execute("SELECT * FROM `menu`")
      data = cursor.fetchall()

      conn.commit()
    except:
      raise Exception("This list does not exists ")
    finally:
      cursor.close()

    for item in data:
      result.append(cls(item[0], item[1]))

    return result

  @classmethod
  def menuById(cls, menuId):
    cursor = conn.cursor()
    data = None

    try:
      cursor.execute("SELECT * FROM `menu` WHERE `menuId` = ?", (menuId, ))
      data = cursor.fetchone()

    except:
      raise Exception("In this list item does not exists")
    finally:
      cursor.close()

    if data is None:
      raise Exception("Not found")

    return cls(data[0], data[1])

  def toJSON(self):
    return {
      "menuId" : self.menuId,
      "title" : self.title
    }

  @property
  def items(self):
    return MenuItem.findByMenu(self.id)

  def add(self, msg):
    return MenuItem.new(msg, self.id)
  

  



