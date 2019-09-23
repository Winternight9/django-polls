from polls.models import Choice

def Votes_count(id):
    vote = 0 
    choice = Choice.objects.all()
    for i in choice:
        if i.question_id == id:
            vote += i.votes  
        else:
            pass
    return vote        