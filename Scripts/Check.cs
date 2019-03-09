using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Check : MonoBehaviour {

	public List<GameObject> CompanyList;
	// Use this for initialization
	void Start () {
		CompanyList=new  List<GameObject> ();
		StartCoroutine(RefreshRight(0,4));
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	
	void OnTriggerEnter(Collider other)
	{
		if(this.name=="Checkin"&&other.gameObject.tag=="Company")
		{
			GameObject newOther = Instantiate(other.gameObject);
			CompanyList.Add(newOther);
			Destroy(other.gameObject);
			//other.transform.parent=GameObject.Find("Right").transform;
		}
		else if (this.name=="Cancel"&&other.gameObject.tag=="Company")
		{
			Destroy(other.gameObject);
		}
		for (int i=0;i<GameObject.Find("Top").transform.childCount;i++)
		{
			GameObject.Find("Top").transform.GetChild(i).GetComponent<BoxCollider>().isTrigger=true;
		}
		InitInfo.GetInstance().aviliable=true;
	}

	void InitCompanyRight(int start,int end)
	{
		for (int i=start ;i<=end;i++)
		{
			if (i<CompanyList.Count)
			{
				CompanyList[i].transform.parent=GameObject.Find("Right").transform;
				CompanyList[i].GetComponent<RectTransform>().localScale=new Vector3(1,1,1);
				CompanyList[i].GetComponent<RectTransform>().localPosition=
			new Vector3(CompanyList[i].GetComponent<RectTransform>().localPosition.x,CompanyList[i].GetComponent<RectTransform>().localPosition.y,0);
			}
		}
	}
	IEnumerator RefreshRight(int start,int end)
	{
		for (int i=0;i<GameObject.Find("Right").transform.childCount;i++)
		{
			if (CompanyList.Count>5)
			{
				Destroy(GameObject.Find("Right").transform.GetChild(i).gameObject);
			}
				
		}
		if (start>=CompanyList.Count)
		{
			InitCompanyRight(0,4);
			start=0;
			end=4;
		}
		else if (end>=CompanyList.Count)
		{
			InitCompanyRight(start,CompanyList.Count-1);
		}
		else
		{
			InitCompanyRight(start,end);
		}
		yield return new WaitForSeconds(3);
		StartCoroutine(RefreshRight(start+5,end+5));
	}
}
