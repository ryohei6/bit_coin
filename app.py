from view import template

currency_list = ["bitcoin", "ethareum"]
page = template.choose_currency_type(currency_list)

if page == "bitcoin":
    template.display_bitcoin_chart()
    
elif page == "ethareum":
    template.display_ethareum_chart()
