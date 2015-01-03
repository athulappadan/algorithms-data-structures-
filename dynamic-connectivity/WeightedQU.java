public class WeightedQU
{
	private int[] id;

	public WeightedQU(int N)
	{
		id = new int[N];
		for (int i = 0; i< N; i++) id[i] = i;
	}

	private int root(int i)
	{
		while(i != id[i])
		{
			id[i]= id[id[i]];
			i = id[i];
		}
		return i;
	}

	private int size(int i)
	{
		int k = 1;
		while(i != id[i])
		{
			i = id[i];
			k++;
		}
		return k;
	}

	public boolean connected(int p, int q)
	{
		return root(p) == root(q);
	}

	public void union(int p, int q)
	{
		int i = root(p);
		int j = root(q);
		if (size(i) < size(j)) id[i] = j;
		else		       id[j] = i;
	}

	public static void main(String args[])
	{
		WeightedQU q = new WeightedQU(10);

		q.union(3,4);
		q.union(4,2);

		boolean a = q.connected(3,2);

		System.out.println(a);
	}
}

