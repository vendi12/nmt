'''
svakulenko
3 Jul 2018

Generate datasets for training and testing NL template learner
'''
import random

# load patterns
with open('search_patterns.txt') as f:
    patterns = f.readlines()
# load search terms
with open('search_terms.txt') as f:
    terms = f.readlines()

random.shuffle(patterns)

for pattern in patterns:
    # shuffle terms
    random.shuffle(terms)
    # generate samples
    user_samples = []
    agent_samples = []
    for i in xrange(len(terms)):
        sample = ''
        search_terms = []
        for c in pattern.strip():
            if c == '*':
                # draw a random search term
                term = terms[i].strip()
                search_terms.append(term)
                sample += term
            else:
                sample += c
        print sample
        user_samples.append(sample)
        agent_samples.append('search ' + ' '.join(search_terms))
    assert len(user_samples) == len(terms) == len(agent_samples)
    
    with open('train.agent', 'a') as f_agent, open('train.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[:40]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[:40]) + '\n')

    with open('dev.agent', 'a') as f_agent, open('dev.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[41:51]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[41:51]) + '\n')

    with open('test.agent', 'a') as f_agent, open('test.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[52:]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[52:]) + '\n')
