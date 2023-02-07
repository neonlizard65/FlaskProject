from flask import Flask, request, Blueprint
from flaskext.mysql import MySQL
import json
from extensions import mysql
from .helper_methods import generate_key, save_image

api = Blueprint('api', __name__)

###############################################################################
#############TODO: MEDIA AND TOKEN ENCRYPTION#################################
##############################################################################

@api.route('/tag', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Tag():
    connect = mysql.connect()
    table = 'Tag'
    pk = 'TagID'
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (Name) VALUES (%s)", (row['Name']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET Name = %s WHERE {table}.{pk} = %s", (row['Name'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {table}.{pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
        
@api.route('/country', methods=['GET'])
def Country():
    table = "Country"
    pk = "CountryID"
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)


@api.route('/build', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Build():
    table = "Build"
    pk="BuildID"
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ProductId, DeveloperUserId, Version, Date, BuildContent, is_demo) VALUES (%s, %s, %s, %s, %s, %s)", (row['ProductId'], row['DeveloperUserId'], row['Version'], row['Date'], row['BuildContent'], row['is_demo']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ProductId = %s, DeveloperUserId = %s, Version = %s, Date = %s, BuildContent = %s, is_demo = %s WHERE {table}.{pk} = %s",  (row['ProductId'], row['DeveloperUserId'], row['Version'], row['Date'], row['BuildContent'], row['is_demo'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

        
@api.route('/cartproduct', methods=['GET', 'POST', 'PUT', 'DELETE'])
def CartProduct():
    table = "CartProduct"
    pk = 'CartProductID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, ProductId) VALUES (%s, %s)", (row['UserId'], row['ProductId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, ProductId = %s WHERE {table}.{pk} = %s",  (row['UserId'], row['ProductId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/cdkey', methods=['GET', 'POST', 'PUT', 'DELETE'])
def CDKey():
    table = "CDKey"
    pk = 'CDKeyID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (Content, ProductId, IsRedeemed) VALUES (%s, %s, %s)", generate_key(), (row['ProductId'], 0))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET Content = %s, ProductId = %s, IsRedeemed=%s WHERE {table}.{pk} = %s",  (row['Content'], row['ProductId'], row['IsRedeemed'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/checkproduct', methods=['GET', 'POST', 'PUT', 'DELETE'])
def CheckProduct():
    table = "CheckProduct"
    pk = 'CheckProductID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (CheckId, ProductId) VALUES (%s, %s)", (row['CheckId'], row['ProductId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET CheckId = %s, ProductId = %s WHERE {table}.{pk} = %s",  (row['CheckId'], row['ProductId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


    
@api.route('/check', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Check():
    table = "Check"
    pk = 'CheckID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, Total, IsRefunded, Date) VALUES (%s, %s, %s, %s)", (row['UserId'], row['Total'], row['IsRefunded'], row['Date']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, Total = %s, IsRefunded=%s, Date=%s WHERE {table}.{pk} = %s",  (row['UserId'], row['Total'], row['IsRefunded'], row['Date'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/contest', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Contest():
    table = "Contest"
    pk = 'ContestID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ContestName, ContestImage, StartDate, EndDate, DeveloperWinner, DevMoneyReward, ContestDescription) VALUES (%s, %s, %s, %s, %s, %s, %s)", (row['ContestName'], row['ContestImage'], row['StartDate'], row['EndDate'], row['DeveloperWinner'], row['DevMoneyReward'], row['ContestDescription']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ContestName = %s, ContestImage = %s, StartDate = %s, EndDate = %s,DeveloperWinner = %s, DevMoneyReward = %s,ContestDescription = %s, WHERE {table}.{pk} = %s",  (row['ContestName'], row['ContestImage'], row['StartDate'], row['EndDate'], row['DeveloperWinner'], row['DevMoneyReward'], row['ContestDescription'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

@api.route('/contestgame', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ContestGame():
    table = "ContestGame"
    pk = 'ContestGameID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ContestId, GameId, VoteCount) VALUES (%s, %s)", (row['ContestId'], row['GameId'], row['VoteCount']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ContestId = %s, GameId = %s, VoteCount = %s, WHERE {table}.{pk} = %s", (row['ContestId'], row['GameId'], row['VoteCount'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/contestpost', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ContestPost():
    table = "ContestPost"
    pk = 'ContestPostID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s LEFT JOIN Post ON {pk} = PostID", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table} LEFT JOIN Post ON {pk} = PostID")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO Post (AuthorUserId, AuthorDevUserId, ProductId, PostDate, Header, TextContent) VALUES (%s, %s, %s, %s,%s, %s)", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent']))   
                cursor.execute(f"SET @lastid = (SELECT PostID from Post ORDER BY PostID DESC LIMIT 1)")         
                cursor.execute(f"INSERT INTO {table} (ContestPostID, ContestId) VALUES (@lastid, %s)", (row['ContestId']))
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE Post SET AuthorUserId = %s, AuthorDevUserId = %s, ProductId = %s, PostDate = %s, Header = %s, TextContent = %s WHERE {table}.{pk} = %s", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent'], row[f'{pk}']))
                cursor.execute(f"UPDATE {table} SET ContestId = %s WHERE {table}.{pk} = %s", (row['ContestId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM Post WHERE {pk} = %s", (row[f'{pk}']))
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/review', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Review():
    table = "Review"
    pk = 'ReviewID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s LEFT JOIN Post ON {pk} = PostID", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table} LEFT JOIN Post ON {pk} = PostID")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO Post (AuthorUserId, AuthorDevUserId, ProductId, PostDate, Header, TextContent) VALUES (%s, %s, %s, %s,%s, %s)", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent']))   
                cursor.execute(f"SET @lastid = (SELECT PostID from Post ORDER BY PostID DESC LIMIT 1)")         
                cursor.execute(f"INSERT INTO {table} (ReviewID, Rating) VALUES (@lastid, %s)", (row['Rating']))
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE Post SET AuthorUserId = %s, AuthorDevUserId = %s, ProductId = %s, PostDate = %s, Header = %s, TextContent = %s WHERE {table}.{pk} = %s", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent'], row[f'{pk}']))
                cursor.execute(f"UPDATE {table} SET Rating = %s WHERE {table}.{pk} = %s", (row['Rating'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM Post WHERE {pk} = %s", (row[f'{pk}']))
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"



@api.route('/newsarticle', methods=['GET', 'POST', 'PUT', 'DELETE'])
def NewsArticle():
    table = "NewsArticle"
    pk = 'NewsArticleID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s LEFT JOIN Post ON {pk} = PostID", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table} LEFT JOIN Post ON {pk} = PostID")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO Post (AuthorUserId, AuthorDevUserId, ProductId, PostDate, Header, TextContent) VALUES (%s, %s, %s, %s,%s, %s)", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent']))   
                cursor.execute(f"SET @lastid = (SELECT PostID from Post ORDER BY PostID DESC LIMIT 1)")         
                cursor.execute(f"INSERT INTO {table} (NewsArticleID, PublisherId, DeveloperId) VALUES (@lastid, %s, %s)", (row['PublisherId'], row['DeveloperId']))
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE Post SET AuthorUserId = %s, AuthorDevUserId = %s, ProductId = %s, PostDate = %s, Header = %s, TextContent = %s WHERE {table}.{pk} = %s", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'],row['Header'],row['TextContent'], row[f'{pk}']))
                cursor.execute(f"UPDATE {table} SET PublisherId = %s WHERE {table}.{pk} = %s", (row['PublisherId'], row['DeveloperId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM Post WHERE {pk} = %s", (row[f'{pk}']))
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/developer', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Developer():
    table = "Developer"
    pk = 'DeveloperID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (DeveloperName, DeveloperLogo, DeveloperBankInfo, DeveloperYoutube, DeveloperTwitch, DeveloperBio, CountryId, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (row['DeveloperName'], row['DeveloperLogo'], row['DeveloperBankInfo'], row['DeveloperYoutube'], row['DeveloperTwitch'], row['DeveloperBio'], row['CountryId'], row['Rating']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET DeveloperName = %s, DeveloperLogo = %s, DeveloperBankInfo = %s, DeveloperYoutube = %s,DeveloperTwitch = %s, DeveloperBio = %s, CountryId = %s, Rating = %s WHERE {table}.{pk} = %s",  (row['DeveloperName'], row['DeveloperLogo'], row['DeveloperBankInfo'], row['DeveloperYoutube'], row['DeveloperTwitch'], row['DeveloperBio'], row['CountryId'], row['Rating'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/developeruser', methods=['GET', 'POST', 'PUT', 'DELETE'])
def DeveloperUser():
    table = "DeveloperUser"
    pk = 'DeveloperUserID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (DeveloperUserName, DeveloperUserPass, DeveloperUserEmail, DeveloperUserGuardCode, DeveloperId, DeveloperUserRole) VALUES (%s, %s, %s, %s, %s, %s)", (row['DeveloperUserName'], row['DeveloperUserPass'], row['DeveloperUserEmail'], row['DeveloperUserGuardCode'], row['DeveloperId'], row['DeveloperUserRole']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET DeveloperUserName = %s, DeveloperUserPass = %s, DeveloperUserEmail = %s, DeveloperUserGuardCode = %s,DeveloperId = %s, DeveloperUserRole = %s WHERE {table}.{pk} = %s",  (row['DeveloperUserName'], row['DeveloperUserPass'], row['DeveloperUserEmail'], row['DeveloperUserGuardCode'], row['DeveloperId'], row['DeveloperUserRole'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

@api.route('/libraryitem', methods=['GET', 'POST', 'PUT', 'DELETE'])
def LibraryItem():
    table = "LibraryItem"
    pk = 'LibraryItemID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, ProductId, CDKeyId, Hours) VALUES (%s, %s, %s, %s)", (row['UserId'], row['ProductId'], row['CDKeyId'], row['Hours']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, ProductId = %s, CDKeyId = %s, Hours = %s {table}.{pk} = %s",  (row['UserId'], row['ProductId'], row['CDKeyId'], row['Hours'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/post', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Post():
    table = "Post"
    pk = 'PostID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (AuthorUserId, AuthorDevUserId, ProductId, PostDate, Header, TextContent) VALUES (%s, %s, %s, %s, %s, %s)", (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'], row['Header'], row['TextContent']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET AuthorUserId = %s, AuthorDevUserId = %s, ProductId = %s, PostDate = %s, Header = %s, TextContent = %s {table}.{pk} = %s",  (row['AuthorUserId'], row['AuthorDevUserId'], row['ProductId'], row['PostDate'], row['Header'], row['TextContent'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/postcomment', methods=['GET', 'POST', 'PUT', 'DELETE'])
def PostComment():
    table = "PostComment"
    pk = 'PostCommentID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, DevUserId, PostId, Content, ReplyToCommentId) VALUES (%s, %s, %s, %s, %s)", (row['UserId'], row['DevUserId'], row['PostId'], row['Content'], row['ReplyToCommentId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, DevUserId = %s, PostId = %s, Content = %s, ReplyToCommentId = %s {table}.{pk} = %s",  (row['UserId'], row['DevUserId'], row['PostId'], row['Content'], row['ReplyToCommentId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/postcommentmedia', methods=['GET', 'POST', 'PUT', 'DELETE'])
def PostCommentMedia():
    table = "PostCommentMedia"
    pk = 'PostCommentMediaID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (PostCommentId, MediaContent) VALUES (%s, %s)", (row['PostCommentId'], row['MediaContent']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET PostCommentId = %s, MediaContent = %s {table}.{pk} = %s",  (row['PostCommentId'], row['MediaContent'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

@api.route('/postmedia', methods=['GET', 'POST', 'PUT', 'DELETE'])
def PostMedia():
    table = "PostMedia"
    pk = 'PostMediaID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (PostId, MediaContent) VALUES (%s, %s)", (row['PostId'], row['MediaContent']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET PostId = %s, MediaContent = %s {table}.{pk} = %s",  (row['PostId'], row['MediaContent'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"



@api.route('/product', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Product():
    table = "Product"
    pk = 'ProductID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f'''INSERT INTO {table} 
                               (Name, ReleaseDate, DeveloperId, PublisherId, Discount, ShortBio, 
                               About, DiscountStartDate, DiscountEndDate, ReviewRating, TotalReviews, PatreonURL) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (row['Name'], row['ReleaseDate'], row['DeveloperId'], row['PublisherId'],row['Discount'], row['ShortBio'],row['About'], row['DiscountStartDate'],row['DiscountEndDate'], row['ReviewRating'],row['TotalReviews'], row['PatreonURL']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET Name = %s, ReleaseDate = %s, DeveloperId = %s, PublisherId = %s, Discount = %s, ShortBio = %s, About = %s, DiscountStartDate = %s, DiscountEndDate = %s, ReviewRating = %s, TotalReviews = %s, PatreonURL = %s {table}.{pk} = %s",  (row['Name'], row['ReleaseDate'], row['DeveloperId'], row['PublisherId'],row['Discount'], row['ShortBio'],row['About'], row['DiscountStartDate'],row['DiscountEndDate'], row['ReviewRating'],row['TotalReviews'], row['PatreonURL'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"



@api.route('/productmedia', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ProductMedia():
    table = "ProductMedia"
    pk = 'ProductMediaID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ProductId, MediaContent) VALUES (%s, %s)", (row['ProductId'], row['MediaContent']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ProductId = %s, MediaContent = %s {table}.{pk} = %s",  (row['ProductId'], row['MediaContent'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/productpricelist', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ProductPriceList():
    table = "ProductPriceList"
    pk = 'PriceListID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ProductId, Price, Currency, Region) VALUES (%s, %s, %s, %s)", (row['ProductId'], row['Price'], row['Currency'], row['Region']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ProductId = %s, Price = %s, Currency=%s, Region=%s WHERE {table}.{pk} = %s",  (row['ProductId'], row['Price'], row['Currency'], row['Region'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/producttag', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ProductTag():
    table = "ProductTag"
    pk = 'ProductTagID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (ProductId, TagId) VALUES (%s, %s)", (row['ProductId'], row['TagId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ProductId = %s, TagId = %s {table}.{pk} = %s",  (row['ProductId'], row['TagId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/publisher', methods=['GET', 'POST', 'PUT', 'DELETE'])
def Publisher():
    table = "Publisher"
    pk = 'PublisherID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (PublisherName, PublisherLogo) VALUES (%s, %s)", (row['PublisherName'], save_image(row['PublisherLogo'], f"{row['PublisherName']}")))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                if row['PublisherLogo'] != None:
                    cursor.execute(f"UPDATE {table} SET PublisherName = %s, PublisherLogo = %s WHERE {table}.{pk} = %s",  (row['PublisherName'], save_image(row['PublisherLogo'], f"{row['PublisherName']}"), row[f'{pk}']))
                else:
                    cursor.execute(f"UPDATE {table} SET PublisherName = %s WHERE {table}.{pk} = %s",  (row['PublisherName'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"



@api.route('/systemrequirement', methods=['GET', 'POST', 'PUT', 'DELETE'])
def SystemRequirement():
    table = "SystemRequirement"
    pk = 'SystemRequirementID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f'''INSERT INTO {table} 
                               (ProductId, IsMinimumRecommended, OS, CPU, RAM, GPU, 
                               DirectX, Storage, SoundCard, Network, AdditionalNotes, Platform) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (row['ProductId'], row['IsMinimumRecommended'], row['OS'], row['CPU'],row['RAM'], row['GPU'],row['DirectX'], row['Storage'],row['SoundCard'], row['Network'],row['AdditionalNotes'], row['Platform']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET ProductId = %s, IsMinimumRecommended = %s, OS = %s, CPU = %s, RAM = %s, GPU = %s, DirectX = %s, Storage = %s, SoundCard = %s, Network = %s, AdditionalNotes = %s, Platform = %s {table}.{pk} = %s",  (row['ProductId'], row['IsMinimumRecommended'], row['OS'], row['CPU'],row['RAM'], row['GPU'],row['DirectX'], row['Storage'],row['SoundCard'], row['Network'],row['AdditionalNotes'], row['Platform'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def User():
    table = "User"
    pk = 'UserId'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f'''INSERT INTO {table} 
                               (UserName, UserPassword, UserEmail, UserPhone, UserAvatar, ProfileBackground, 
                               IsPrivate, StatusId, UserRealName, UserCountryId, Bio, EmailSubscription, LastOnline, UserBotToken, CashbackBonus) 
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (row['UserName'], row['UserPassword'], row['UserEmail'], row['UserPhone'], save_image(row['UserAvatar'], f"{row['UserName']}_avatar"), save_image(row['ProfileBackground'], f"{row['UserName']}_background"),row['IsPrivate'], row['StatusId'],row['UserRealName'], row['UserCountryId'],row['Bio'], row['EmailSubscription'], row['LastOnline'], row['UserBotToken'], row['CashbackBonus']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserName = %s, UserPassword = %s, UserEmail = %s, UserPhone = %s, UserAvatar = %s, ProfileBackground = %s, IsPrivate = %s, StatusId = %s, UserRealName = %s, UserCountryId = %s, Bio = %s, EmailSubscription = %s, LastOnline = %s, UserBotToken = %s, CashbackBonus = %s {table}.{pk} = %s",  (row['UserName'], row['UserPassword'], row['UserEmail'], row['UserPhone'],row['UserAvatar'], row['ProfileBackground'],row['IsPrivate'], row['StatusId'],row['UserRealName'], row['UserCountryId'],row['Bio'], row['EmailSubscription'], row['LastOnline'], row['UserBotToken'], row['CashbackBonus'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
        
        
@api.route('/userlike', methods=['GET', 'POST', 'PUT', 'DELETE'])
def UserLike():
    table = "UserLike"
    pk = 'UserLikeID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, PostId, CommentId) VALUES (%s, %s, %s)", (row['UserId'], row['PostId'], row['CommentId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, PostId = %s, CommentId = %s {table}.{pk} = %s",  (row['UserId'], row['PostId'], row['CommentId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
        
        
@api.route('/usernewspreference', methods=['GET', 'POST', 'PUT', 'DELETE'])
def UserNewsPreference():
    table = "UserNewsPreference"
    pk = 'UserNewsPreferenceID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, DeveloperId, PublisherId, ProductId) VALUES (%s, %s, %s, %s)", (row['UserId'], row['DeveloperId'], row['PublisherId'], row['ProductId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, DeveloperId = %s, PublisherId = %s, ProductId=%s {table}.{pk} = %s",  (row['UserId'], row['DeveloperId'], row['PublisherId'], row['ProductId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"


@api.route('/uservote', methods=['GET', 'POST', 'PUT', 'DELETE'])
def UserVote():
    table = "UserVote"
    pk = 'UserVoteID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, ContestPostId, ContestGameId) VALUES (%s, %s, %s)", (row['UserId'], row['ContestPostId'], row['ContestGameId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, ContestPostId = %s, ContestGameId = %s {table}.{pk} = %s",  (row['UserId'], row['ContestPostId'], row['ContestGameId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"

@api.route('/cartproduct', methods=['GET', 'POST', 'PUT', 'DELETE'])
def WishlistProduct():
    table = "WishlistProduct"
    pk = 'WishlistProductID'
    connect = mysql.connect()
    if request.method == 'GET':
        id = request.args.get(f'{pk}')
        cursor = connect.cursor()
        if id is not None:
            cursor.execute(f"SELECT * FROM {table} WHERE {pk} = %s", id)
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchone()
            cursor.close()
            data = []
            data.append(dict(zip(headers, res)))
            return json.dumps(data, default=str)
        else:
            cursor.execute(f"SELECT * FROM {table}")
            headers = [x[0] for x in cursor.description]
            res = cursor.fetchall()
            cursor.close()
            data = []
            for row in res:
                data.append(dict(zip(headers, row)))
            return json.dumps(data, default=str)
    elif request.method == 'POST':
        try:
            record = json.loads(request.data)
            cursor = connect.cursor()
            for row in record:
                cursor.execute(f"INSERT INTO {table} (UserId, ProductId) VALUES (%s, %s)", (row['UserId'], row['ProductId']))   
            connect.commit()
            cursor.close()
            return "Success"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'PUT':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"UPDATE {table} SET UserId = %s, ProductId = %s WHERE {table}.{pk} = %s",  (row['UserId'], row['ProductId'], row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
    elif request.method == 'DELETE':
        try:
            cursor = connect.cursor()
            record = json.loads(request.data)
            if record[0][f'{pk}'] == None:
                raise f"Didn't include {pk}"
            for row in record:
                cursor.execute(f"DELETE FROM {table} WHERE {pk} = %s", (row[f'{pk}']))
            connect.commit()
            cursor.close()
            return "OK"
        except Exception as ex:
            return f"Error: {ex}"
