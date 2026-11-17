"""解释已取得原文中的客户意向强度业务上下文。"""
from .evidence import records

def snapshot(db,known_at):
    rows=records(db,'context',known_at)
    if not rows:return None
    p=rows[-1]['payload']
    return {'customer':p['customer'],'commitment':p['commitment'],'project':p['project'],'vessels':p['vessels']}

def eligible(s,d,state,period):
    if state is None:return False,'缺少业务上下文'
    return (d.get('customer',state['customer'])==state['customer'],'客户身份不匹配')

def metrics(allocations,state,period):
    if state is None:return {'context_gap':'缺少业务上下文'}
    return {'signal_strength':state['commitment'],'project':state['project'],'vessel_count':state['vessels']}
