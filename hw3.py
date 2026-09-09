
is_logged_in=True;
print(is_logged_in)
is_subscribed=False;
print(is_subscribed)
user_credits=100;
max_credits=200;
min_credits=50;
credit_valid = (min_credits < user_credits <= max_credits) and ( user_credits!= min_credits);
print(credit_valid);

bonus_eligible=is_subscribed  or not user_credits<= min_credits;
print(bonus_eligible);

user_credits+=50;
user_credits-=20;
user_credits*=2;
user_credits%=150;
print(user_credits);

power_result=user_credits**2;
print(power_result)

full_access= is_logged_in and is_subscribed;
print(full_access);

is_true_login= is_logged_in is True;
print(is_true_login);

access_result = is_logged_in or is_subscribed and False
print(access_result)
