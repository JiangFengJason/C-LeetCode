using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InitInfo : MonoBehaviour {
	// static InitInfo instance;
    // public static InitInfo Instance
    // {
    //     get
    //     {
    //         //if (instance == null)
    //         //    instance = this;
    //         return instance;
    //     }
    // }
	private static InitInfo _instance = null;

    public static InitInfo GetInstance()
    {
        if (_instance == null)
        {
            _instance = new InitInfo();
        }
        return _instance;
    }
	public Camera camera;
    public Vector3 [] corners;
	public GameObject top;
	public GameObject right;
	public GameObject company;
	public Sprite [] companys;
	public bool aviliable;
	// Use this for initialization
	void Start () {
		//top left
        corners[0] = camera.ViewportToWorldPoint(new Vector3(0, 1, 2));
        //top right
        corners[1] = camera.ViewportToWorldPoint(new Vector3(1, 1, 2));
        //bottom left
        corners[2] = camera.ViewportToWorldPoint(new Vector3(0, 0, 2));
        //bottom right
        corners[3] = camera.ViewportToWorldPoint(new Vector3(1, 0, 2));

		companys=Resources.LoadAll<Sprite>("Company"+"/");
		
		aviliable=true;
		InitPos();

		if (companys.Length>5)
			StartCoroutine(RefreshTop(0,4));
		else
			InitCompany(0,companys.Length-1);
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	private void InitPos()
	{
		top.GetComponent<RectTransform>().sizeDelta=new Vector2((corners[1].x-corners[0].x)*0.8f/0.15f,5);
		top.GetComponent<RectTransform>().localPosition=new Vector3(0,corners[1].y-1f,10);
		right.GetComponent<RectTransform>().sizeDelta=new Vector2(5,(corners[1].y-corners[3].y)*0.8f/0.15f);
		right.GetComponent<RectTransform>().localPosition=new Vector3(corners[1].x-1,0,10);
	}
	private void InitCompany(int start,int end)
	{
		
		for (int i=start;i<=end;i++)
		{
			GameObject newCompany = Instantiate(company);
			newCompany.GetComponent<BoxCollider>().isTrigger=aviliable;
			newCompany.name=companys[i].name;
			newCompany.GetComponent<SpriteRenderer>().sprite=companys[i];
			newCompany.transform.parent=GameObject.Find("Top").transform;
			newCompany.GetComponent<RectTransform>().localScale=new Vector3(1,1,1);
			newCompany.GetComponent<RectTransform>().localPosition=
			new Vector3(newCompany.GetComponent<RectTransform>().localPosition.x,newCompany.GetComponent<RectTransform>().localPosition.y,0);
		}
		
	}

	IEnumerator RefreshTop(int start,int end)
	{
		for (int i=0;i<GameObject.Find("Top").transform.childCount;i++)
		{
			Destroy(GameObject.Find("Top").transform.GetChild(i).gameObject);
		}
		if (start>=companys.Length)
		{
			InitCompany(0,4);
			start=0;
			end=4;
		}
		else if (end>=companys.Length)
		{
			InitCompany(start,companys.Length-1);
		}
		else
		{
			InitCompany(start,end);
		}
	
		yield return new WaitForSeconds(3);
		StartCoroutine(RefreshTop(start+5,end+5));
	}
}
