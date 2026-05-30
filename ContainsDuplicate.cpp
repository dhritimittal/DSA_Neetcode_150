class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //sort the array
        sort(nums.begin(), nums.end());
        //check if every element is equal to the element before it
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == nums[i - 1]){
                return true;
            }
        }
        return false;
    }
};
