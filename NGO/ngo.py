from flask import *
from database import *
import uuid
from datetime import datetime,date

ngo=Blueprint('ngo',__name__)

@ngo.route('/ngohome')
def ngohome():
	return render_template("ngohome.html")


@ngo.route('/ngoaddwork',methods=['get','post'])
def ngoaddwork():
	data={}
	q="select * from work"
	res=select(q)
	data['event']=res

	if 'add' in request.form:
		event=request.form['event']
		description=request.form['description']
		# a=request.form['a']
		q="insert into work values(null,'%s','%s','0',curdate(),'pending','0')"%(event,description)
		insert(q)
		return redirect(url_for('ngo.ngoaddwork'))
	return render_template('ngoaddwork.html',data=data)


@ngo.route('/ngoviewproposal',methods=['get','post'])
def ngoviewproposal():
	data={}
	work_id=request.args['work_id']

	q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where work_id='%s'"%(work_id)
	res=select(q)
	data['view']=res
	# if res[0]['status']=='pending':
	# 	flash('not approved proposals')
	# 	return redirect(url_for('ngo.ngoaddwork'))

	# else:
	# 	data['view']=res

	return render_template("ngoviewproposal.html",data=data)


@ngo.route('/ngoviewalocatedretailerdetail')
def ngoviewalocatedretailerdetail():
	data={}
	retailer_id=request.args['retailer_id']
	q="select * from retailer where retailer_id='%s'"%(retailer_id)
	res=select(q)
	data['view']=res
	return render_template("ngoviewalocatedretailerdetail.html",data=data)

# @ngo.route('/ngoviewhomeinspection')
# def ngoviewhomeinspection():
# 	data={}
# 	id=request.args['id']
# 	q="select * from inspection where worker_id='%s'" %(id)
# 	res=select(q)
# 	data['inspection']=res

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		wid=request.args['wid']
# 	else:
# 		action=None
# 	if action=="accept":
# 		q="update inspection set status='accept' where inspection_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewhomeinspection',id=id))
# 	if action=="reject":
# 		q="update inspection set status='reject' where inspection_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewhomeinspection',id=id))

# 	return render_template("ngoviewhomeinspection.html",data=data)



# @ngo.route('/ngoviewimmunization')
# def ngoviewimmunization():
# 	data={}
# 	id=request.args['id']
# 	q="select * from immunization where worker_id='%s'" %(id)
# 	res=select(q)
# 	data['immunization']=res

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		wid=request.args['wid']
# 	else:
# 		action=None
# 	if action=="accept":
# 		q="update immunization set status='accept' where immunization_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewimmunization',id=id))
# 	if action=="reject":
# 		q="update immunization set status='reject' where immunization_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewimmunization',id=id))
		
# 	return render_template("ngoviewimmunization.html",data=data)

# @ngo.route('/ngoviewhealthreport')
# def ngoviewhealthreport():
# 	data={}
# 	# id=request.args['id']
# 	# q="select * from health where worker_id='%s'" %(id)
# 	q="select * from health "
# 	res=select(q)
# 	data['health']=res

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		wid=request.args['wid']
# 	else:
# 		action=None
# 	if action=="accept":
# 		q="update health set status='accept' where health_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewhealthreport',id=id))
# 	if action=="reject":
# 		q="update health set status='reject' where health_id='%s'" %(wid)
# 		update(q)
# 		return redirect(url_for('ngo.ngoviewhealthreport',id=id))

# 	return render_template("ngoviewhealthreport.html",data=data)



# @ngo.route('/ngoviewfamilymember')
# def ngoviewfamilymember():
# 	data={}
# 	id=request.args['id']
# 	q="select * from family_members inner join user using(user_id) where worker_id='%s'"%(id)
# 	res=select(q)
# 	data['attendance']=res
# 	return render_template("ngoviewfamilymember.html",data=data)


# @ngo.route('/ngoviewPregnant')
# def ngoviewPregnant():
# 	data={}
# 	id=request.args['id']
# 	q="select * from pregnant where `family_member_id`='%s'"%(id)
# 	res=select(q)
# 	data['attendance']=res
# 	return render_template("ngoviewPregnant.html",data=data)



# @ngo.route('/ngoprintreport',methods=['get','post'])
# def ngoprintreport():
# 	data={}
# 	today=date.today()
# 	print(today)
# 	data['today']=today
# 	now=datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print(current_time)
# 	data['current_time']=current_time	
# 	q="SELECT * FROM family_members INNER JOIN `health` USING(family_member_id)"
# 	r=select(q)
# 	data['view']=r
	
# 	return render_template('ngoprintreport.html',data=data)