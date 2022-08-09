from flask import *
from database import *
import uuid
from datetime import datetime,date

retailer=Blueprint('retailer',__name__)

@retailer.route('/retailerhome')
def retailerhome():
	return render_template("retailerhome.html")





@retailer.route('/retailerviewwork',methods=['get','post'])
def retailerviewwork():
	data={}
	q="select * from work"
	res=select(q)
	data['view']=res
	
	return render_template("retailerviewwork.html",data=data)


@retailer.route('/retailersendproposal',methods=['get','post'])
def retailersendproposal():
	data={}
	work_id=request.args['work_id']
	if 'add' in request.form:
		# re=request.form['re']
		a=request.form['a']
		
		q="insert into proposal values(null,'%s','%s','%s',curdate(),'pending')"%(work_id,session['retailer_id'],a)
		insert(q)

		flash('proposal send successfully')

		return redirect(url_for('retailer.retailersendproposal',work_id=work_id))
	q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where work_id='%s' and retailer_id='%s' "%(work_id,session['retailer_id'])
	data['view']=select(q)
	# q="SELECT * FROM retailer"
	# data['rview']=select(q)


	return render_template("retailersendproposal.html",data=data)





@retailer.route('/retailerviewproposal',methods=['get','post'])
def retailerviewproposal():
	data={}
	work_id=request.args['work_id']
	q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where  retailer_id='%s' and work_id='%s' "%(session['retailer_id'],work_id)
	data['view']=select(q)
	


	return render_template("retailerviewproposal.html",data=data)
