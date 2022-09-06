class Solution:
  def invalidTransactions(self, transactions):
    result = []
    records = []

    for t in transactions:
        # split the record rec = [name, time, amt, city]
        rec = t.split(',')
        # convert to ints
        rec[1] = int(rec[1])
        rec[2] = int(rec[2])
        # add to records list
        records.append(rec)

    for rec in records:
        print("starting record: ", rec)
        # amount > 1000$
        if rec[2] > 1000:
            rec[1] = str(rec[1])
            rec[2] = str(rec[2])
            # add to list
            result.append(','.join(rec))
            continue
        
        # iterate all records to look for 2nd condition
        for x in records:
            # if name matches and time is in window and city doesn't match
            # Making sure cities don't match avoids adding a record matching itself
            if rec[0] == x[0] and abs(rec[1]-int(x[1])) <= 60 and rec[3] != x[3]:
                rec[1] = str(rec[1])
                rec[2] = str(rec[2])
                # add to list
                result.append(','.join(rec))
                break

            
    return result
