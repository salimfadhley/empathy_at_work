ALL_QUESTIONS =list(map(lambda x:x.strip(), filter(lambda line: line.strip(), """
Facts always come above feelings when giving feedback.
I find I am most productive at work in the morning.
People often tell me I am blunt.
People often come to me for advice on personal issues.
I get easily frustrated when clients/customers talk about non related work issues.
I find it easy making conversation with customers or clients I haven't met before.
I often daydream at work.
In meetings I tend to focus on my own thoughts rather than my impact on other people.
I respect the decision of the people I work with even if I don't agree with them.
I'd rather drive to work than take public transport.
I'd rather solve my own problems than ask someone for help.
I worry about getting the right tone in emails.
It's important to me that I get along with all my colleagues.
I often think about what I'm going to have for dinner whilst I am at work.
Structure and hierarchy is vital in businesses.
I prefer to keep emails and texts short and to the point.
I like to express my personality at work.
I often wish my colleagues would get to the point when in conversation with them.
I enjoy having a joke with my colleagues.
I'd rather search for facts than get an opinion from a colleague.
I find structure and routine essential to my day at work.
I think empathy in a working environment is important.
I like working with data and numbers.
I avoid social situations at work.
I like to have my day at work planned out before I get there.
I'd have no idea how to respond if a colleague cried.
I prefer to work with computers than people.
I am naturally good at small talk.
Sensing people's moods and emotions comes naturally to me.
I care about what my colleagues think of me.
I'm uninterested in workplace politics.
I like to find meaning through my work.
I find motivating my team easy.
Work is not a place to show emotions.
I try to put my colleagues needs before my own.
I enjoy talking about my home life at work.
I prefer working individually than collaborating as a team.
Its more important to get individual recognition than team recognition at work.
""".splitlines())))

POSITIVE_SCORING_SCHEME = {
    "definitely agree":2,
    "agree":1
}

NEGATIVE_SCORING_SCHEME = {
    "definitely disagree":2,
    "disagree":1
}


class Scorer(object):

    @classmethod
    def build_scorer_from_uncompiled_strategy(cls, uncompiled_strategy):
        strategy = {}

        for one_biased_questions, scoring_scheme in uncompiled_strategy:
            for one_biased_question_index in one_biased_questions:
                question = ALL_QUESTIONS[one_biased_question_index -1]
                strategy[question] = scoring_scheme

        return cls(strategy)

    def __init__(self, strategy):
        self.strategy = strategy

    def score_row(self, row):
        score = 0
        for column_name, scoring_scheme in self.strategy.items():
            row_value = row[column_name]
            score += scoring_scheme.get(row_value, 0)
        return score

EQ_SCORER = Scorer.build_scorer_from_uncompiled_strategy([
    (set([4, 9, 12, 17, 22, 30, 32, 35]), POSITIVE_SCORING_SCHEME),
    (set([3, 11,18, 20, 23, 24, 26]), NEGATIVE_SCORING_SCHEME)
])

SQ_SCORER = Scorer.build_scorer_from_uncompiled_strategy([
    (set([1, 5, 8, 15, 16, 21, 27, 34, 37, 38]), POSITIVE_SCORING_SCHEME),
    (set([6, 13, 28, 29, 33]), NEGATIVE_SCORING_SCHEME)
])

if __name__ == "__main__":
    import pprint

    pprint.pprint(EQ_SCORER.strategy)

    pprint.pprint(SQ_SCORER.strategy)