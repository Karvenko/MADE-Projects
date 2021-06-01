#include <stdio.h>

typedef long long ll_int;

const ll_int MOD_16 = 1LL << 16;
const ll_int MOD_30 = 1LL << 30;

void fill_cum_sum(ll_int* cum_sum, ll_int n, ll_int x, ll_int y, ll_int a0)
{
    ll_int i, a_prev;
    
    cum_sum[0] = a0;
    a_prev = a0;
    for (i = 1; i < n; i++)
    {
        a_prev = (x * a_prev + y) % MOD_16;
        cum_sum[i] = cum_sum[i - 1] + a_prev;
    }
}

ll_int get_next_b(ll_int b_prev, ll_int z, ll_int t)
{
    return ((z * b_prev + t) % MOD_30 + MOD_30) % MOD_30;
}

ll_int process_req(ll_int* cum_sum, ll_int n, ll_int m, ll_int z, ll_int t, ll_int init_b0)
{
    ll_int i;
    ll_int b0, b1, c0, c1, left, right;
    ll_int result = 0;
    
    b0 = init_b0;
    b1 = get_next_b(b0, z, t);
    
    for (i = 0; i < m; i++)
    {
        c0 = b0 % n;
        c1 = b1 % n;
        if (c0 < c1)
        {
            left = c0;
            right = c1;
        }
        else
        {
            left = c1;
            right = c0;
        }
        
        if (left == 0)
        {
            result += cum_sum[right];
        }
        else
        {
            result += cum_sum[right] - cum_sum[left - 1];
        }
        
        b0 = get_next_b(b1, z, t);
        b1 = get_next_b(b0, z, t);
    }
    return result;    
}

int main()
{
    ll_int n, x, y, a0;
    ll_int m, z, t, b0;
    ll_int* cum_sum;
    
    scanf("%lld%lld%lld%lld", &n, &x, &y, &a0);
    scanf("%lld%lld%lld%lld", &m, &z, &t, &b0);
    
    cum_sum = new long long[n];
    fill_cum_sum(cum_sum, n, x, y, a0);
    
    printf("%lld\n", process_req(cum_sum, n, m, z, t, b0));
    
    return 0;
}
