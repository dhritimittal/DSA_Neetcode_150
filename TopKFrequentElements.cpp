class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //create a dictionary and keep increasing the count value when the key appears in array
        unordered_map<int, int> count;
        for(int num : nums){
            count[num]++;
        }
        
        // initialise array to store the key value pairs from dictionary storing value first, key second
        vector<pair<int, int>> arr;
        for(const auto& p : count){
            arr.push_back({p.second, p.first});
        }
        
        //sort the array in descending order
        sort(arr.rbegin(), arr.rend());
        
        //initialise a result array and push the top k elements
        vector<int> res;
        for(int i = 0; i < k; ++i){
            res.push_back(arr[i].second);
        }
        return res;
    }
};
