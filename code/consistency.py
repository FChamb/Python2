'''
First 3 basic requirements
1. Check the consistency of the initial (raw) data.
2. Output refined data for further analysis, fixing any encountered inconsistencies.
3. Provide an executable Python script to automate the two steps above.

– develop a procedure to check that the data match expected format, remove duplicates, and
perform further refinement. This procedure should check that:
1. the file exists and is readable as expected;
2. the values of variables are of the expected format (numbers, strings, etc.);
3. the values of variables are admissible (e.g. are within a given range or are from the list
of admissible values);
4. there are no logical contradictions in the data.
– in case of any inconsistencies and/or duplicates found, produce new file with refined data
to be used in the subsequent analysis (doing the checks is important, event if the data will
not have instances of all problems you might anticipate)
– this step must be automated to the point when it can be run with a single shell command to
call an executable Python script specifying necessary arguments
'''