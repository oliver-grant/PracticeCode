#include <thread>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <assert.h>
#include <mutex>

struct node {
  int val;
  node *next;
  node *prev;
  node(int v, node* n, node* p) {
    val = v;
    next = n;
    prev = p;
  }
  
};


class my_queue {

private:
  node *_front = NULL;
  node *_back = NULL;
  std::mutex _mut; 

public:
  void push(int n) {
    std::unique_lock<std::mutex> mlock(_mut);
    node *temp = new node(n, NULL, NULL);
    if (_front == NULL) {
      _front = temp;
      _back = temp;
    } else {
      node* old_back = _back;
      _back = temp;
      temp->next = old_back;
      old_back->prev = temp;
    }
    mlock.unlock();
  }

  int pop_front() {
    std::unique_lock<std::mutex> mlock(_mut);
    if (_front == NULL) {
      return -1;
      mlock.unlock();    }
    
    int ret = _front->val;
    node* old_front = _front;
    _front = _front->prev;
    if(_front != NULL) _front->next = NULL;
    if (old_front == _back) {
      _back = NULL;
    }
    delete old_front;
    mlock.unlock();
    return ret;
  }
  
  int peek_front() {
    std::unique_lock<std::mutex> mlock(_mut);
    int ret = _front->val;
    mlock.unlock();
    return ret;
  }


  void print() {
    std::unique_lock<std::mutex> mlock(_mut);
    for (node* n = _back; n != NULL; n = n->next) {
      std::cout << n->val << std::endl;
    }
    std::cout << std::endl;
    mlock.unlock();
  }
};

void n_push(class my_queue *q) {
  for (int i = 0; i < 100; ++i) {
    q->push(i);
  }
}


int main() {
  my_queue q;
  assert(q.pop_front() == -1);
  q.print();
  q.push(6);
  q.print();
  q.push(9);
  q.print();
  q.push(15);
  q.print();
  std::cout << std::endl;
  std::cout << q.peek_front() << std::endl;
  q.pop_front();
  q.print(); 
  std::cout << q.peek_front() << std::endl << std::endl;
  q.pop_front();
  std::cout << q.peek_front() << std::endl;
  q.pop_front();

  std::thread t1(n_push, &q);
  std::thread t2(n_push, &q);
  t1.join();
  t2.join();
  
  q.print();

}
