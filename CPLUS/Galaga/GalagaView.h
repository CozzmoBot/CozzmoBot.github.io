
// GalagaView.h : CGalagaView Ŭ������ �������̽�
//

#pragma once


class CGalagaMap;

class CGalagaView : public CView
{
protected: // serialization������ ��������ϴ�.
	CGalagaView();
	DECLARE_DYNCREATE(CGalagaView)

// Ư���Դϴ�.
public:
	CGalagaDoc* GetDocument() const;
	CGalagaMap *m_pMap;

	void StartThread();
	void StopThread();
	void SuspendThread();
	void ResumeThread();

	void Restart();

private:	

	bool m_bFlag;
	bool m_bSuspend;
	CWinThread *m_pMyBullet;
	CWinThread *m_pMoveThread;
	CWinThread *m_pDrawThread;

	// Thread Func
	
	static UINT BulletThread(LPVOID p);
	static UINT DrawThread(LPVOID p);
	static UINT KeyDownThread(LPVOID p);

// �۾��Դϴ�.
public:

// �������Դϴ�.
public:
	virtual void OnDraw(CDC* pDC);  // �� �並 �׸��� ���� �����ǵǾ����ϴ�.
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);

// �����Դϴ�.
public:
	virtual ~CGalagaView();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// ������ �޽��� �� �Լ�
protected:
	DECLARE_MESSAGE_MAP()
public:
	virtual void OnInitialUpdate();
	afx_msg void OnKeyDown(UINT nChar, UINT nRepCnt, UINT nFlags);
	afx_msg BOOL OnEraseBkgnd(CDC* pDC);
	afx_msg void OnDestroy();

	LRESULT OnRestart(WPARAM wparam, LPARAM lparam);
};

#ifndef _DEBUG  // GalagaView.cpp�� ����� ����
inline CGalagaDoc* CGalagaView::GetDocument() const
   { return reinterpret_cast<CGalagaDoc*>(m_pDocument); }
#endif

