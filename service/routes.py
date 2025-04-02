@app.route('/products/<int:id>', methods=['GET'])
def read_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.serialize())

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.price = data.get('price', product.price)
    db.session.commit()
    return jsonify(product.serialize())
