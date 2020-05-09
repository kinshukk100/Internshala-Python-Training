class book:
     def init (self,aut, pub, p, cp=0):
         self.author=aut
         self.publisher=pub
         self.price=p
         self.copies=cp
     def get_author(self):
         return self._author
     def set_author(self, aut):
         self._author=aut
         return
     author=property(get_author, set_author)
     def get_publisher(self):
         return self._publisher
     def set_publisher(self, pub):
         self._publisher=pub
         return
     publisher=property(get_publisher, set_publisher)
     def get_price(self):
         return self._price
     def set_price(self,p):
         self._price=p
         return
     price=property(get_price, set_price)
     def get_copies(self):
         return self._copies
     def set_copies(self,cp):
         self._copies=cp
         return
     copies=property(get_copies, set_copies)

     def get_royalty(self):
         if self.copies<=500:
             self._royalty=self.copies*self.price*10/100
         elif self.copies<=1000:
             self._royalty=500*self.price*10/100+\(self.copies-500)*self .price*12.5/100
         else:
             self._royalty=500*self.price*10/100 + \ 500*self.price*12.5/100 + \(self.copies-1000)*self.price*15/100
         return self._royalty

 class ebook(book):
     def __init__(self, aut, pub, p, cp=0, form=None):
         super().__init__(aut,pub,p,cp)
         self.format=form
     def get_format(self):
         return self._format
     def set_format(self, form):
         self._format=form
         return
     format=property(get_format, set_format)
     def get_royalty(self):
         ryl=super().get_royalty()
         ryl=ryl-ryl*12/100
         self._royalty=ryl
         return self._royalty

 if __name__== "__main__":
     print ('print book example')
     b1=book('aa','ss',100,600)
     print ("Royalty earned : ", b1.get_royalty())
     print ('ebook example')
     e1=ebook('aa','ss',100, 3, 'PDF')
     print ('Royalty earned' , e1.get_royalty())
