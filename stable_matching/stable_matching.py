#The women that men prefer
preferred_rankings_men = {'ryan': ['lizzy','sarah','zoey','daniella'],
                          'josh': ['sarah','lizzy','daniella','zoey'],
                          'blake': ['sarah','daniella','zoey','lizzy'],
                          'connor': ['lizzy','sarah','zoey','daniella']
                          }
#The men that women prefer
preferred_rankings_women = {'lizzy': ['ryan','blake','josh','connor'],
                            'sarah': ['ryan','blake','connor','josh'],
                            'zoey': ['connor','josh','ryan','blake'],
                            'daniella': ['ryan','josh','connor','blake']
                            }
#keeps track of people that may end up together
tentative_engagements = []

#free men
free_men=[]

def init_free_men():
    for man in preferred_rankings_men.iterkeys():
        free_men.append(man)
        
def stable_matching():
    while len(free_men)>0:
        for man in free_men:
            begin_matching(man)

def begin_matching(man):
    print 'dealing with %s'%man
    for woman in preferred_rankings_men[man]:
        taken_match=[couple for couple in tentative_engagements if woman in couple]
        if (len(taken_match) == 0):
            tentative_engagements.append([man,woman])
            free_men.remove(man)
            print '%s is no longer a free men and is now tentatively engaged to %s'%(man,woman)
            break
        elif (len(taken_match)) > 0:
              print '%s is already taken..'%(woman)

              current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
              potential_guy = preferred_rankings_women[woman].index(man)

              if (current_guy < potential_guy):
                  print 'she is satisfied with %s..'%(taken_match[0][0])
              else:
                  print '%s is better than %s'%(man,taken_match[0][0])
                  print 'making %s free again... and then tentatively accept engagement between %s and &s'%(taken_match[0][0],man,woman)
                  free_men.remove(man)
                  free_men.append(token_match[0][0])
                  token_match[0][0]=man
                  break
def main():
    init_free_men()
    stable_matching()
    print 'complete list of couples\n'
    print tentative_engagements

if __name__=='__main__':
    main()
