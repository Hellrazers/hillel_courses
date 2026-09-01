
laptop_variable = 'Ноутбук Acer Aspire Lite AL15-54P-53SQ (NX.DTHEU'

red_price_of_laptop = f'''//*[contains(@title, "{laptop_variable}") and @rztiletitle]/following-sibling::div//div[@class="price text-2xl color-red"]'''