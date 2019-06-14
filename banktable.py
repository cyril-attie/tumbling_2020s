# /usr/local/bin/python3.7

'''prints a table describing the evolution of the quantity of money when a bank appears
use provide optional parameters

'''
import sys
import pprint


def main(sim_duration=300, sim_inflation_interest=0.025, sim_deflation_interest=0.06):
    years = list(range(sim_duration+1))
    inflation_deflation_periods = int(((sim_duration+1)/5)+1)
    issued_bills = [0]
    for j in range(1, inflation_deflation_periods):
        issued_bills += [4 * j for i in range(5)] + [0 for i in range(5)]
    returned_bills = [0] 
    for l in [  [0 for i in range(5)]+[4+p*2 for i in range(5)] for p in range(inflation_deflation_periods)]: 
      returned_bills += l
    existing_bills = [100]
    circulating_bills = [100]
    bills_in_bank = [0]
    debt_bal_before_int = [0]
    current_year_int_pctg = [sim_inflation_interest] + (
      [sim_inflation_interest for i in range(5)] + [sim_deflation_interest for i in range(5)]) * inflation_deflation_periods
   
    current_year_interest = [0]
    debt_bal_after_int = [0]

    table= {'years':years, 
            'existing_bills':existing_bills, 
            'circulating_bills':circulating_bills,
            'bills_in_bank': bills_in_bank,
            'issued_bills': issued_bills,
            'returned_bills':returned_bills,
            'debt_bal_before_int':debt_bal_before_int,
            'current_year_int_pctg':current_year_int_pctg,
            'current_year_interest':current_year_interest,
            'debt_bal_after_int':debt_bal_after_int}

    for i in range(1, sim_duration+1):
        circulating_bills.append(
            circulating_bills[-1]+issued_bills[i]-returned_bills[i])
        if issued_bills[i] != 0 and issued_bills[i] > bills_in_bank[-1]:
            existing_bills.append(
                existing_bills[-1] + issued_bills[i] - bills_in_bank[-1])
            bills_in_bank.append(0)
        elif issued_bills[i] != 0 and issued_bills[i] < bills_in_bank[-1]:
            existing_bills.append(existing_bills[-1])
            # if including simultaneous issue and return +returned_bills[i]
            bills_in_bank.append(bills_in_bank[-1]-issued_bills[i])
        else:  # when no issued bills, deflation case
            existing_bills.append(existing_bills[-1])
            bills_in_bank.append(bills_in_bank[-1]+returned_bills[i])
        debt_bal_before_int.append(
            round(debt_bal_after_int[-1]+issued_bills[i]-returned_bills[i], 3))
        current_year_interest.append(
            round(current_year_int_pctg[i] * debt_bal_before_int[i], 3))
        debt_bal_after_int.append(
            round(debt_bal_before_int[i] + current_year_interest[i], 3))

    return {'years':years, 
            'existing_bills':existing_bills, 
            'circulating_bills':circulating_bills,
            'bills_in_bank': bills_in_bank,
            'issued_bills': issued_bills,
            'returned_bills':returned_bills,
            'debt_bal_before_int':debt_bal_before_int,
            'current_year_int_pctg':current_year_int_pctg,
            'current_year_interest':current_year_interest,
            'debt_bal_after_int':debt_bal_after_int}

def display_table(data):
  titles = ['YEAR', 'EXISTING BILLS',  'IN CIRCULATION', 'IN THE BANK',
              'ISSUED YoY', 'RETURNED YoY', 'DBAL BEG OF Y', 'INT%', 'INTEREST', 'DBAL BEG OF Y']

  for t in titles:
      print(t, end='\t')
  print('')
  for i in range(len(data['years'])):
      if i <= 50 or i%25 == 0:
          for x in data.keys():
              print(round(data[x][i], 3), end='\t')
          print('\n')


if __name__ == '__main__':
    # automatic example when used from the command line

    sim_duration = 30
    sim_inflation_interest = 0.05
    sim_deflation_interest = 0.1

    if len(sys.argv) == 1:
        pass
    if len(sys.argv) >= 2:
        sim_duration = int(sys.argv[1])
    if len(sys.argv) >= 3:
        sim_inflation_interest = float(sys.argv[2])
    if len(sys.argv) >= 4:
        sim_deflation_interest = float(sys.argv[3])

    print(sim_duration, sim_inflation_interest, sim_deflation_interest)
    bt = main(sim_duration, sim_inflation_interest, sim_deflation_interest)
    display_table(bt)
 