import boto3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'my_table'
table = dynamodb.Table(table_name)

@app.route('/', methods=['GET', 'POST'])
def display_table():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        city = request.form['city']
        new_item = {'name': name, 'age': age, 'city': city}
        
        # Store the new item in DynamoDB table
        table.put_item(Item=new_item)
        
        return redirect('/')
    
    # Retrieve all items from DynamoDB table
    response = table.scan()
    items = response.get('Items', [])
    
    return render_template('table.html', items=items)

@app.route('/delete', methods=['POST'])
def delete_entry():
    index = int(request.form['index'])
    
    # Retrieve all items from DynamoDB table
    response = table.scan()
    items = response.get('Items', [])
    
    if index < len(items):
        # Get the item to be deleted based on the index
        item = items[index]
        
        # Delete the item from DynamoDB table
        table.delete_item(Key=item)
    
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
