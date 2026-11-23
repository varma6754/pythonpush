'''Mobile Recharge System

Scenario: A user has ₹500 in their wallet.

Requirements:
- Display available balance.
- Ask for recharge amount.
- Check wallet balance.
- Deduct recharge amount.
- Allow multiple recharges.
- Stop when the user chooses exit.'''

wallet_balance=500
plans={'unlimited':49,'1GB':22,'monthly':349}
while True:
    print(plans)
    plan_name=input("enter the recharge plan: ")
    if plan_name in plans:
        p_n=plans.get(plan_name)
        if p_n>wallet_balance:
            print("insufficient balance")
        else:
            wallet_balance=wallet_balance-p_n
        repeat=input("do you want add on (yes/no): ")
        if repeat=='yes':
            continue
        else:
            break
    else:
        print("invalid plan")
        continue
print("wallet balance: ",wallet_balance)