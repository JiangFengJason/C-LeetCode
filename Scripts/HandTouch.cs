using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HandTouch : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}
	
	void OnTriggerEnter(Collider other)
	{
		if (other.gameObject.tag=="Company")
		{
			GameObject clone = Instantiate(other.gameObject);
			clone.GetComponent<BoxCollider>().isTrigger=false;
			for (int i=0;i<GameObject.Find("Top").transform.childCount;i++)
			{
				GameObject.Find("Top").transform.GetChild(i).GetComponent<BoxCollider>().isTrigger=false;
			}
			InitInfo.GetInstance().aviliable=false;
			clone.transform.parent=GameObject.Find("HandColliderLeft").transform;
			clone.GetComponent<RectTransform>().localPosition=new Vector3(0,0,0);
			clone.GetComponent<RectTransform>().localScale=new Vector3(0.3f,0.3f,1);
		}
	}
}
