task_intro = f"""
Your task is to write a short biography about a fallen solider from WWII. The biography should only draw on facts given to you in \
the reference material, delimited by ```. If a date, name, or other detail is not included in the reference material or \
this prompt, do NOT include it in the biography. Do not make assumptions.
"""

key_detail_list =f"""
- Full Name
- Birth date
- Birth place
- Interesting details about home life (schooling, occupation, acheivements, etc.)
- Were they married? If so, did they have children?
- Date of enlistment
- Rank 
- Branch of service
- Death date
- Death place
- Cause of death
- Burial location
- Father's name
- Mother's name
- How many brothers and sisters
- Interesting details about family members (parent's occupation, other siblings that served in the millitary, etc.) 
"""

story_structure = f"""
Once you have noted any facts found in the reference text, write a 5 paragraph biography about the fallen solider. \
(If there is not enough information for 5 paragraphs, write 3 paragraphs instead.) The biography \
should be both educational and fun to read. Only include details that are directly related to the fallen solider and his/her \
experience. Always be respectful of the fallen and their sacrifice. 

The first sentence should include the fallen's full name, birth date, and birth place (if provided). The rest of the first paragraph \
should describe any details about the fallen's childhood and family.

In the following paragraphs, refer to the fallen by their title and last name. Describe the fallen's enlistment date, their time serving, \
and the situations surrounding their death. The final paragraph should give their death date, death place, cause of death, \
and location of burial (if provided).
"""

sbts_credit = f"""
Include a one more paragraph with the exact wording delimited in the <>. 
<This story is part of the Stories Behind the Stars project (see www.storiesbehindthestars.org/) . This is a national effort of \
volunteers to write the stories of all 400,000+ of the US WWII fallen here on Fold3. Can you help write these stories? Related to this, \
there will be a smart phone app that will allow people to visit any war memorial or cemetery, scan the fallen's name and read his/her story.>
"""
