---
title: "Big O"
weight: 0
---

# Big O / Time Complexity Practice


## Determining Big O

For the following examples, assume the correct libraries have been imported.

### Level 1

#### Method 1

```java
private int[] one_one(int N) {
    int k = 0;
    int m = i;
    int[] nums;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            nums = new int[5];
        }
    }
    return nums;
} 
```

#### Method 2

```java
private int one_two(int N) {
    int j = 1;
    int count = 0;
    while (j < 1_000_000) {
        for (int i = 1; i <= N; i++) {
            j += N / i + 1;
        }
        count += 1;
    }
    return count;
} 
```

#### Method 3

Assume **N == data.length** and that **arrayCopy** is \\( O(N) \\) and **Arrays.sort** is \\( O(Nlog_2(N)) \\)

```java
private int one_three(int[] data) {
    int count = 0;
    for (int i = 0; i < data.length; i++) {
        int[] tmp = arrayCopy(data);
        count += tmp[i];
        Arrays.sort(tmp);
        count += tmp[i];
    }
    return count;
} 

private int[] arrayCopy(int[] arr) {
    // Returns a copy of arr without modifying arr
}
```

### Level 2

#### Method 1

Assume **N == data.length** and **Arrays.sort** is \\( O(Nlog_2(N)) \\)

```java
private void two_one(int[] data) {
    for (int i = 1; i < data.length; i *= 3) {
        Arrays.sort(arrayCopy(data));
    }
} 

private int[] arrayCopy(int[] arr) {
    // Returns a copy of arr without modifying arr
}
```

#### Method 2

```java
private float two_two(int N) {
    float weirdNum = 3;
    for (int i = N; i > 0; i--) {
        weird_num += 2;
        // This does some stuff ... who knows what
        for (int j = i - 1; j < i; j++) {
            weirdNum *= j * 10.0 / N + 1;
        }
        i *= -1;
        weird_num -= 1;
        if (((int) weird_num % 2) == 0) {
            weirdNum *= -1;
        }
    }
    return weirdNum;
} 
```

#### Method 3

```java
private void two_three(int N) {
    int count = 0;
    for (int k = 0; k < N * N; k++) {
        for (int j = 0; j < Math.sqrt(N); j++) {
            count += 1;
        }
    }
} 
```

### Level 3

#### Method 1

```java
private void three_one(int[] data) {
    for (int i = 0; i < data.length; i++) {
        for (int j = 0; j < data.length; j++) {
            insertionSort(data);
        }
    }
}

// From: https://medium.com/@soni.dumitru/
// insertion-sort-algorithm-java-script-655483dd22c2
private void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int temp = a[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j -= 1;
        }
        arr[j + 1] = temp;
    }
}
```

#### Method 2

```java
private void three_two(int N) {
    int r = 0;
    for (int i = 1; i < N; i *= 2) {
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < N; k++) {
                r += 1;
            }
        }
    }
    return r;
}
```

## Answers

### Determining Big O

#### Level 1

{{<katex>}}
1) \; O(N^2)\\
2) \; O(N)\\
3) \; O(N^2\log_2(N))\\
{{</katex>}}

#### Level 2

{{<katex>}}
1) \; O(N \cdot log_2(N) \cdot log_3(N))\\
2) \; O(1)\\
3) \; O(N^{5/2})\\
{{</katex>}}

#### Level 3

{{<katex>}}
1) \; O(N^3)\\
2) \; O(N^2)\\
{{</katex>}}