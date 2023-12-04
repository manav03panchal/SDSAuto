test.py will take an array of chemical names, and then make requests to API (public) to find a CAS# for it. The code will then return a csv file with name of chemical
and the CAS # (blank if not found) 

some simple RegEx can be used to refine the chemical names a bit, so that the API can find matches. 

So far with testing I have not seen any issues and it is quite accurate if the chemical name is matching. Some complex names can cause issues, so little manual oversight is 
required. 
