#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

int bottomUp(int weights[], int values[], int i,int j, vector<vector<int>>& memoBU){

    if(i < 0 or j < 0){
        return 0;
    }
    int newj = j - 1;
    int newi = i - weights[j];
    if(weights[j] > i + 1){
        memoBU[i][j] = bottomUp(weights, values, i, newj, memoBU);
    }
    else{
        int val1 = values[j] + bottomUp(weights, values, newi, newj, memoBU);
        int val2 = bottomUp(weights, values, i, newj, memoBU);
        memoBU[i][j] = (val1 > val2) ? val1 : val2;
    }
    return memoBU[i][j];
}

void solve(){
    int n, W;
    cin >> n >> W;

    int weights[n];
    int values[n];

    for(int i = 0; i < n; i++){
        cin >> weights[i];
    }
    for(int i = 0; i < n; i++){
        cin >> values[i];
    }
    vector<int> memoRow(n, -1);
    vector<vector<int>> memoBU(W, memoRow); 

    cout << bottomUp(weights, values, W - 1, n - 1, memoBU) << endl;
    // print(bottomUp(W - 1, n - 1))
}

int main(){
    int t = 1;
    while(t--){
        solve();
    }
    return 0;
}