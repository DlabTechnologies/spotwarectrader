 $(function() {
 	
	  
	
	
	
	$.plot('#flotChart3', [{
		data: flotSampleData5,
		color: '#5965f9',
		fillColor:'rgb(0, 123, 255,0.5)',
	}], {
		series: {
			shadowSize: 0,
			lines: {
				show: true,
				lineWidth: 2,
				fill: true,
				fillColor: {
					colors: [{
						opacity: 0
					}, {
						opacity: 0.4,
					}]
				}
			}
		},
		grid: {
			borderWidth: 0,
			labelMargin: 0
		},
		yaxis: {
			show: false,
			min: 0,
			max: 110,
			color: '#e2eaf9'
		},
		xaxis: {
			show: false,
			color: '#e2eaf9'
		}
	});
	
	$.plot('#flotChart5', [{
		data: flotSampleData2,
		color: '#ff5959',
		fillColor:'rgba(255, 89, 89,0.5)'
	}], {
		series: {
			shadowSize: 0,
			lines: {
				show: true,
				lineWidth: 2,
				fill: true,
				fillColor: {
					colors: [{
						opacity: 0
					}, {
						opacity: 0.4,
					}]
				}
			}
		},
		grid: {
			borderWidth: 0,
			labelMargin: 0
		},
		yaxis: {
			show: false,
			min: 0,
			max: 130,
			color: '#e2eaf9'
		},
		xaxis: {
			show: false,
			color: '#e2eaf9'
		}
	});
	
	$.plot('#flotChart1', [{
		data: flotSampleData4,
		color: '#0acf97',
		fillColor:'rgb(15, 189, 102,0.1)',
	}], {
		series: {
			shadowSize: 0,
			lines: {
				show: true,
				lineWidth: 2,
				fill: true,
				fillColor: {
					colors: [{
						opacity: 0
					}, {
						opacity: 0.4,
					}]
				}
			}
		},
		grid: {
			borderWidth: 0,
			labelMargin: 0
		},
		yaxis: {
			show: false,
			min: 0,
			max: 110,
			color: '#e2eaf9'
		},
		xaxis: {
			show: false,
			color: '#e2eaf9'
		}
	});
	
	
	
	
	   var plot = $.plot($('#flotChart12'), [
        {
            data: flotSampleData4,
            label: 'Balance',
            color: '#5965f9'
        }],
        {
            series: {
                lines: {
                    show: true,
                    lineWidth: 2,
                    fill: true,
                    fillColor: { colors: [{ opacity: 0 }, { opacity: .7 }] }
                },
                shadowSize: 1
            },
            points: {
                show: false,
            },
            legend: {
                noColumns: 1,
            },
            grid: {
                hoverable: true,
                clickable: true,
                borderWidth: 0,
                labelMargin: 5
            },
            yaxis: {
                 ticks: [[0, ''], [15, '$6320'], [30, '$6340'], [45, '$6360'], [60, '$6380'], [75, '$6400']],
                min: 0,
                max: 65,
                color: 'rgba(0,0,0,.070)',
                font: {
                    size: 10,
                    color: '#777777'
                }
            },
            xaxis: {
                ticks: [[0, '06:00'], [20, '09:00'], [40, '12:00'], [60, '13:00'], [80, '16:00'], [100, '19:00'], [120, '21:00'], [140, '23:00']],
                color: 'rgba(0,0,0,.070)',
                font: {
                    size: 10,
                    color: '#777777'
                }
            }
        });
		
		
		
		const ps5 = new PerfectScrollbar('.transcation-scroll', {
		   useBothWheelAxes:true,
		   suppressScrollX:true,
		});
	

 });