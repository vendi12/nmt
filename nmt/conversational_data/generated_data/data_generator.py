'''
svakulenko
3 Jul 2018

Generate datasets for training and testing NL template learner
'''
import random

# load patterns
with open('search_patterns.txt') as f:
    patterns = f.readlines()

random.shuffle(patterns)

for pattern in patterns:
    # load search terms
    with open('search_terms.txt') as f:
        terms = f.readlines()
        # shuffle terms
        random.shuffle(terms)
    # generate samples
    user_samples = []
    agent_samples = []
    while terms:
        sample = ''
        search_terms = []
        for c in pattern.strip():
            if c == '*':
                # draw a random search term
                term = terms.pop().strip()
                search_terms.append(term)
                sample += term
            else:
                sample += c
        print sample
        user_samples.append(sample)
        agent_samples.append('search ' + ' '.join(search_terms))
    
    with open('train.agent', 'a') as f_agent, open('train.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[:30]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[:30]) + '\n')

    with open('dev.agent', 'a') as f_agent, open('dev.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[31:41]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[31:41]) + '\n')

    with open('test.agent', 'a') as f_agent, open('test.user', 'a') as f_user:
        f_user.writelines('\n'.join(user_samples[42:]) + '\n')
        f_agent.writelines('\n'.join(agent_samples[42:]) + '\n')
