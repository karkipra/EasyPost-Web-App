from flask import Flask, render_template, request
import easypost as EasyPost

# Test API key: EZTK74c21deaf5cf4ee991473a59941dd1c1nQlauL0pcG8PFEgeEdRvyA
EasyPost.api_key = 'EZTK74c21deaf5cf4ee991473a59941dd1c1nQlauL0pcG8PFEgeEdRvyA'
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    # Create and verify addresses
    try:
        from_address = EasyPost.Address.create(
            verify=["delivery"],
            name=request.form['name_1'],
            street1=request.form['street1_1'],
            street2=request.form['street2_1'],
            city=request.form['city_1'],
            state=request.form['state_1'],
            zip=request.form['zip_1'],
            country=request.form['country_1'],
            phone=request.form['phone_1']
        )
        to_address = EasyPost.Address.create(
            verify=["delivery"],
            name=request.form['name_2'],
            street1=request.form['street1_2'],
            street2=request.form['street2_2'],
            city=request.form['city_2'],
            state=request.form['state_2'],
            zip=request.form['zip_2'],
            country=request.form['country_2'],
            phone=request.form['phone_2']
        )
        # create parcel
        try:
            parcel = EasyPost.Parcel.create(
                predefined_package=request.form['predefine'],
                weight=request.form['weight']
            )
        except EasyPost.Error as e:
            print(str(e))
            if e.param is not None:
                print('Specifically an invalid param: %r' % e.param)

        parcel = EasyPost.Parcel.create(
            length=request.form['length'],
            width=request.form['width'],
            height=request.form['height'],
            weight=request.form['weight']
        )
        # create shipment
        shipment = EasyPost.Shipment.create(
            to_address=to_address,
            from_address=from_address,
            parcel=parcel,
            customs_info=customs()
        )
    except EasyPost.Error as e:
        return render_template('result.html', e=e)

    # Shipment label url
    shipment.buy(rate=shipment.lowest_rate())
    shipping_label = shipment.postage_label.label_url
    print(shipping_label)
    return render_template('result.html', s=shipping_label)


def customs():
    # create customs_info form for international shipping
    # put in default values from API
    customs_item = EasyPost.CustomsItem.create(
        description="EasyPost t-shirts",
        hs_tariff_number=123456,
        origin_country="US",
        quantity=2,
        value=96.27,
        weight=21.1
    )
    customs_info = EasyPost.CustomsInfo.create(
        customs_certify=1,
        customs_signer="Hector Hammerfall",
        contents_type="gift",
        contents_explanation="",
        eel_pfc="NOEEI 30.37(a)",
        non_delivery_option="return",
        restriction_type="none",
        restriction_comments="",
        customs_items=[customs_item]
    )


if __name__ == '__main__':
    app.run(debug=True)
