import sys

loan = {
    'amount': 12000
}

year = {
    '2021': { 
        'styczen': 1.592824484,
        'luty': -0.453509101,
        'marzec': 2.324671717,
        'kwiecien': 1.261254404,
        'maj': 1.782526286,
        'czerwiec': 2.329384541,
        'lipiec': 1.502229842,
        'sierpien': 1.782526286,
        'wrzesien': 2.328848994,
        'pazdziernik': 0.616921348207244,
        'listopad': 2.35229588637833,
        'grudzien': 0.337779545187098,
    },
    
    '2022': {
        'styczen': 1.57703524727525,
        'luty': -0.292781442607648, 
        'marzec': 2.48619659017508, 
        'kwiecien': 0.267110317834564,
        'maj': 1.41795267229799,
        'czerwiec': 1.05424326726375,
        'lipiec': 1.4805201044812,
        'sierpien': 1.57703524727525,
        'wrzesien': -0.0774206903147018,
        'pazdziernik': 1.16573339872354,
        'listopad': -0.404186717638335,
        'grudzien': 1.49970852083123,
    }
}

''' (1+(({inflation}+{percent_above_inflation})/1200))*{loan_amount}-{installment_amount} '''

def main(percent_above_inflation, installment_amount):
    for x in year.values():
        for key, value in x.items():
            last_amount = loan['amount']
            # print(f"{key}" + " -----> " + f"{( 1 + (( float(value) + float(percent_above_inflation)) / 1200 )) * float(loan['amount']) - float(installment_amount)}")
            new_amount = ( 1 + (( float(value) + float(percent_above_inflation)) / 1200 )) * float(loan['amount']) - float(installment_amount)
            loan.update({'amount': ( 1 + (( float(value) + float(percent_above_inflation)) / 1200 )) * float(loan['amount']) - float(installment_amount)})
            diff_amount = last_amount - new_amount
            print(f"Twoja pozostała kwota kredytu to {new_amount}, to {diff_amount} mniej niż w poprzednim miesiącu.")

if __name__ == "__main__":
    if len(sys.argv) <= 2 or len(sys.argv) >= 4:
        print("Enter the param as:")
    else:
        main(sys.argv[1], sys.argv[2])