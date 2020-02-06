# buggy-quicksort

This is a (buggy) example of QuickSort’s partition function. This demo is generate a test case to check if the test case will trigger the
bug in the partition function. It will print path that is exercised by the test case.

``` c++
void partition (int a[ ], int n) {
    int pivot = a[0];
    left = 0;
    right = n-1;
    
    while (left < right){
        while (a[right] >= pivot)
            right--;
        
        if (left != right){
            a[left] = a[right];
            left++;
        }
        
        while (a[left] < pivot)
            left++;
        
        if (left != right){
            a[right] = a[left];
            right--;
        }
    }
    a[left] = pivot;
}
```

## Run
```shell
$ python3 demo.py
```
```shell
a[]: [3, 1, 2, 3] , n:  4
path: 1->2->3->4->5->6->5->7->8->9->10->11->10->11->10->12->13->14->4->15->end
a[]: [2, 1, 3, 3]
```
