class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      //create a hash table  
      unordered_map<int, int> map;
        //check if the required number is already in the hash table. if yes, return the index of the required element from hash table and the current index.
        for(int i = 0; i < nums.size(); i++){
            int p = target - nums[i];
            if (map.count(p)){
                return {map[p], i};
            }
            //if required element is not in hash table, then add the current element to the table.
            map.insert({nums[i], i});
            //or
            //map[nums[i]] = i; 
        }      
        return {};
    }
};
