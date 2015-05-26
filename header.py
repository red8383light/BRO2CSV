#!/usr/bin/python2

app_stats="ts,ts_delta,app,uniq_hosts,hits,bytes"
communication="ts,peer,src_name,connected_peer_desc,connected_peer_addr,connected_peer_port,level,message"
conn="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,service,duration,orig_bytes,resp_bytes,conn_state,local_orig,missed_bytes,history,orig_pkts,orig_ip_bytes,resp_pkts,resp_ip_bytes,tunnel_parents"
dns="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,trans_id,query,qclass,qclass_name,qtype,qtype_name,rcode,rcode_name,AA,TC,RD,RA,Z,answers,TTLs,rejected"
dhcp="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,mac,assigned_ip,lease_time,trans_id"
dpd="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,analyzer,failure_reason"
files="ts,fuid,tx_hosts,rx_hosts,conn_uids,source,depth,analyzers,mime_type,filename,duration,local_orig,is_orig,seen_bytes,total_bytes,missing_bytes,overflow_bytes,timedout,parent_fuid,md5,sha1,sha256,extracted"
ftp="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,user,password,command,arg,mime_type,file_size,reply_code,reply_msg,data_channel.passive,data_channel.orig_h,data_channel.resp_h,data_channel.resp_p,fuid"
http="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,trans_depth,method,host,uri,referrer,user_agent,request_body_len,response_body_len,status_code,status_msg,info_code,info_msg,filename,tags,username,password,proxied,orig_fuids,orig_mime_types,resp_fuids,resp_mime_types,client_header_names,server_header_names,cookie_vars,uri_vars"
irc="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,nick,user,command,value,addl,dcc_file_name,dcc_file_size,dcc_mime_type,fuid"
intel="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,fuid,file_mime_type,file_desc,seen.indicator,seen.indicator_type,seen.where,sources"
kerberos="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,request_type,client,service,success,error_msg,from,till,cipher,forwardable,renewable,client_cert_subject,client_cert_fuid,server_cert_subject,server_cert_fuid"
known_certs="ts,host,port_num,subject,issuer_subject,serial"
known_devices="ts,mac,dhcp_host_name"
known_hosts="ts,host"
known_services="ts,host,port_num,port_proto,service"
loaded_scripts="name"
modbus="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,func,exception"
mysql="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,cmd,arg,success,rows,response"
notice="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,fuid,file_mime_type,file_desc,proto,note,msg,sub,src,dst,p,n,peer_descr,actions,suppress_for,dropped,remote_location.country_code,remote_location.region,remote_location.city,remote_location.latitude,remote_location.longitude"
packet_filter="ts,node,filter,init,success"
pe="ts,id,machine,compile_ts,os,subsystem,is_exe,is_64bit,uses_aslr,uses_dep,uses_code_integrity,uses_seh,has_import_table,has_export_table,has_cert_table,has_debug_data,section_names"
radius="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,username,mac,remote_ip,connect_info,result"
rdp="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,cookie,result,security_protocol,keyboard_layout,client_build,client_name,client_dig_product_id,desktop_width,desktop_height,requested_color_depth,cert_type,cert_count,cert_permanent,encryption_level,encryption_method"
reporter="ts,level,message,location"
signatures="ts,src_addr,src_port,dst_addr,dst_port,note,sig_id,event_msg,sub_msg,sig_count,host_count"
sip="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,trans_depth,method,uri,date,request_from,request_to,response_from,response_to,reply_to,call_id,seq,subject,request_path,response_path,user_agent,status_code,status_msg,warning,request_body_len,response_body_len,content_type"
smtp="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,trans_depth,helo,mailfrom,rcptto,date,from,to,reply_to,msg_id,in_reply_to,subject,x_originating_ip,first_received,second_received,last_reply,path,user_agent,fuids,is_webmail"
snmp="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,duration,version,community,get_requests,get_bulk_requests,get_responses,set_requests,display_string,up_since"
socks="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,version,user,status,request.host,request.name,request_p,bound.host,bound.name,bound_p"
software="ts,host,host_p,software_type,name,version.major,version.minor,version.minor2,version.minor3,version.addl,unparsed_version,url"
ssh="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,status,direction,client,server,remote_location.country_code,remote_location.region,remote_location.city,remote_location.latitude,remote_location.longitude"
ssl="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,version,cipher,server_name,session_id,subject,issuer_subject,not_valid_before,not_valid_after,last_alert,client_subject,client_issuer_subject,cert_hash,validation_status"
syslog="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,proto,facility,severity,message"
top_websites="ts,ts_delta,where,top_sites,top_counts,top_epsilons"
traceroute="ts,src,dst,proto"
tunnel="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,tunnel_type,action"
weird="ts,uid,id.orig_h,id.orig_p,id.resp_h,id.resp_p,name,addl,notice,peer"
x509="ts,id,certificate.version,certificate.serial,certificate.subject,certificate.issuer,certificate.not_valid_before,certificate.not_valid_after,certificate.key_alg,certificate.sig_alg,certificate.key_type,certificate.key_length,certificate.exponent,certificate.curve,san.dns,san.uri,san.email,san.ip,basic_constraints.ca,basic_constraints.path_len"
