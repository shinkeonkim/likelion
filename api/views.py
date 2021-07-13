from django.shortcuts import render
from django.http import HttpResponse
from .utils import ordinal_number

def likelion_shield_badge(request):
  generation = request.GET.get('generation') or 9

  svg = '''
  <svg height="20" width="110" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.37 20">
    <defs>
      <style>
        .cls-1,.cls-3 {{
          fill: #231815;
        }}
        .cls-2 {{
          fill: #f39800;
        }}
        .cls-3 {{
          isolation:isolate;font-size:13px;font-family:GillSans-SemiBold, Gill Sans;font-weight:600;
        }}
        .cls-4{{
          fill:#f29f00;
        }}
      </style>
    </defs>
    <g id="레이어_2" data-name="레이어 2">
      <g id="레이어_1-2" data-name="레이어 1">
        <g id="레이어_2-2" data-name="레이어 2">
          <g id="레이어_1-2-2" data-name="레이어 1-2">
            <g id="레이어_1-2-2-2" data-name="레이어 1-2-2">
              <path class="cls-1" d="M3.63,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H3.63A3.6,3.6,0,0,1,0,16.44V3.56A3.6,3.6,0,0,1,3.63,0Z"/>
              <path class="cls-2" d="M67.3,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H67.3"/>
              <text class="cls-3" text-anchor="middle" transform="translate(83.79 14.35)">
                {generation_ordinal_number}
              </text>
            </g>
          </g>
        </g>
        <polygon class="cls-4" points="4.2 5.63 6.11 5.63 6.11 12.62 10.61 12.62 10.61 14.35 4.2 14.35 4.2 5.63"/>
        <rect class="cls-4" x="11.72" y="5.63" width="1.92" height="8.72"/>
        <polygon class="cls-4" points="15.05 5.63 16.97 5.63 16.97 9.37 20.51 5.63 22.82 5.63 19.27 9.33 22.99 14.35 20.68 14.35 17.98 10.63 16.97 11.68 16.97 14.35 15.05 14.35 15.05 5.63"/>
        <polygon class="cls-4" points="23.7 5.63 30.49 5.63 30.49 7.33 25.59 7.33 25.59 9.13 30.27 9.13 30.27 10.84 25.59 10.84 25.59 12.64 30.49 12.64 30.49 14.35 23.7 14.35 23.7 5.63"/>
        <polygon class="cls-4" points="33.91 5.63 35.83 5.63 35.83 12.62 40.32 12.62 40.32 14.35 33.91 14.35 33.91 5.63"/><rect class="cls-4" x="41.42" y="5.63" width="1.92" height="8.72"/>
        <polygon class="cls-4" points="54.76 5.63 56.6 5.63 60.69 11 60.69 5.63 62.67 5.63 62.67 14.35 60.95 14.35 56.73 8.8 56.73 14.35 54.76 14.35 54.76 5.63"/>
        <path class="cls-4" d="M49,14.59a4.82,4.82,0,0,1-1.89-.36,4.76,4.76,0,0,1-1.49-1,4.49,4.49,0,0,1-1-1.44A4.62,4.62,0,0,1,44.3,10v0a4.42,4.42,0,0,1,.35-1.78,4.69,4.69,0,0,1,1-1.46,4.56,4.56,0,0,1,1.5-1A4.89,4.89,0,0,1,49,5.41a4.82,4.82,0,0,1,1.89.36,4.65,4.65,0,0,1,1.49,1,4.33,4.33,0,0,1,1,1.44A4.63,4.63,0,0,1,53.73,10v0a4.59,4.59,0,0,1-1.34,3.24,4.56,4.56,0,0,1-1.5,1,4.86,4.86,0,0,1-1.89.36m0-1.76a2.67,2.67,0,0,0,1.1-.22A2.61,2.61,0,0,0,51,12a2.76,2.76,0,0,0,.55-.9,2.8,2.8,0,0,0,.2-1.08v0a2.82,2.82,0,0,0-.2-1.09A2.59,2.59,0,0,0,51,8a2.68,2.68,0,0,0-.87-.61,2.78,2.78,0,0,0-2.19,0,2.73,2.73,0,0,0-.85.6,2.76,2.76,0,0,0-.55.9A3,3,0,0,0,46.3,10v0a3,3,0,0,0,.2,1.09,2.59,2.59,0,0,0,.56.9,2.87,2.87,0,0,0,.86.61,2.64,2.64,0,0,0,1.1.23"/>
      </g>
    </g>
  </svg>'''.format(
      generation_ordinal_number=ordinal_number(generation),
    )

  response = HttpResponse(content=svg)
  response['Content-Type'] = 'image/svg+xml'
  response['Cache-Control'] = 'no-cache'
  return response
