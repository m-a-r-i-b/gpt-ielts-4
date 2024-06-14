from utils import delimiter, separate_score_and_feedback
import math
from criteria.TaskResponse import assess_task_response 
from criteria.CoherenceAndCohesion import assess_coherence_and_cohesion 
from criteria.LexicalResource import assess_lexical_resource 
from criteria.GrammaticalRangeAndAccuracy import assess_grammatical_range_and_accuracy 


sample_user_query = f"""
Doing an enjoyable activity with a child can develop better skills and more creativity than reading. To what extent do you agree? Use reasons and specific examples to explain your answer.
{delimiter}
Parents throughout the world place spend time reading with their offspring to prepare them for school where their literacy skills are further developed; however, recent research suggests that focusing on reading at an early age can be detrimental, and participating in fun activities would be far more beneficial. I am a strong advocate of this approach, and the benefits of it will be covered in this essay.

A fundamental reason for this is that there is no biological age for reading, and pushing infants to acquire this skill before they are ready could have repercussions. For example, in the UK, many boys are reluctant readers, possibly because of being forced to read, and this turned them off reading. By focusing on other activities and developing other skills such as creativity and imagination, when they are ready to read, they usually acquire this skill rapidly.

In addition, the importance of encouraging creativity and developing a child's imagination must be acknowledged. Through play, youngsters develop social and cognitive skills, for example, they are more likely to learn vocabulary through context rather than learning it from a book.

Furthermore, play allows youngsters to mature emotionally, and gain self-confidence. There is no scientific research which suggests reading at a young age is essential for a child's development, moreover, evidence suggests the reverse is true. In Finland, early years' education focuses on playing.

Reading is only encouraged if a child shows an interest in developing this skill. This self-directed approach certainly does not result in Finnish school leavers falling behind their foreign counterparts. In fact, Finland was ranked the sixth-best in the world in terms of reading.

Despite being a supporter of this non-reading approach, I strongly recommend incorporating bedtime stories into a child's daily routine. However, reading as a regular daytime activity should be swapped for something which allows the child to develop other skills.
"""


task_response_raw_result = assess_task_response(sample_user_query)
tr_score, tr_feedback = separate_score_and_feedback(task_response_raw_result)

coherence_and_cohesion_raw_result = assess_coherence_and_cohesion(sample_user_query)
cc_score, cc_feedback = separate_score_and_feedback(coherence_and_cohesion_raw_result)

lexical_resource_raw_result = assess_lexical_resource(sample_user_query)
lr_score, lr_feedback = separate_score_and_feedback(lexical_resource_raw_result)

grammatical_range_and_accuracy_raw_result = assess_grammatical_range_and_accuracy(sample_user_query)
gr_score, gr_feedback = separate_score_and_feedback(grammatical_range_and_accuracy_raw_result)


overall_score = math.ceil((tr_score + cc_score + lr_score + gr_score)/4)
overall_feedback = f"""
Task Response {tr_score} : {tr_feedback} \n
Coherence and Cohesion {cc_score} : {cc_feedback} \n
Lexical Resource {lr_score} : {lr_feedback} \n
Grammatical range and Accuracy {gr_score} : {gr_feedback} \n
"""

print(overall_score)
print(overall_feedback)