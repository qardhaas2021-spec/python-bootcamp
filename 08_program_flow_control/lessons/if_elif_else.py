train = 'rail 109'
departure_city = 'dublin'
arrival_city = 'sligo'
ticket_price = 8.50
passanger_age = 17
has_ticket = True
train_statues = 'on time'
seat_available = True

# check if passanger has a ticket

if has_ticket:
    print(f'ticket found for {departure_city} to {arrival_city}')

else:
    print('No tivket please buy a ticket')

# check age for discount

if passanger_age < 18:
    ticket_price = 0
    print(f'you are a  minor and you get a discount of {ticket_price}')
elif passanger_age > 18:
    ticket_price = 10
    print(f'you are an adult and you get a discount of {ticket_price}')
elif passanger_age >= 65:
    ticket = ticket_price * 0.5
    print(f'you are a senior and you get a discount of {ticket_price}')
else:
    print('you are not eligibkle for a discount')
    

data = [1, 2, 3, 10, 20, 15, 23, 14]
mean = sum(data) / len(data)
mode = max(data, key=data.count)
meadian = sorted(data)[len(data) // 2]
interquartile_range = sorted(data)[len(data) // 4] - sorted(data)[len(data) // 4]
print(f'mean: {mean}, mode: {mode}, meadian: {meadian}, interquartile range: {interquartile_range}')





